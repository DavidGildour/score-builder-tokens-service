from .utils import get_json_content


USER = {'user_id': '0', 'role': 'ADMIN'}

def get_token(client, user_id, role):
    resp = client.get(f'/token?user_id={user_id}&role={role}')
    return get_json_content(resp)['access_token']

def test_generating_tokens(client):
    resp = client.get('/token?user_id={user_id}&role={role}'.format(**USER))

    assert '200' in resp.status

def test_getting_id_from_token(client):
    token = get_token(client, **USER)

    resp = client.get('/user_id',
                      headers=dict(
                          Authorization=f'Bearer {token}'
                      ))
    user_id = get_json_content(resp)['user_id']

    assert user_id == USER['user_id']

def test_getting_role_from_token(client):
    token = get_token(client, **USER)

    resp = client.get('/user_role',
                      headers=dict(
                          Authorization=f'Bearer {token}'
                      ))
    user_role = get_json_content(resp)['user_role']

    assert user_role == USER['role']

def test_using_revoked_token(client):
    token = get_token(client, **USER)

    resp = client.get('/blacklist',
                      headers=dict(
                          Authorization=f'Bearer {token}'
                      ))

    assert 200 == resp.status_code

    resp = client.get('/user_role',
                      headers=dict(
                          Authorization=f'Bearer {token}'
                      ))

    assert '401' in resp.status

    resp = client.get('/user_id',
                      headers=dict(
                          Authorization=f'Bearer {token}'
                      ))

    assert '401' in resp.status