from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt_claims, get_raw_jwt

from blacklist import BLACKLIST


class GetToken(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('user_id', required=True)
    parser.add_argument('role', required=True)

    @classmethod
    def get(cls):
        data = cls.parser.parse_args()

        return {
            'access_token': create_access_token(identity=data['user_id'], user_claims={'role': data['role']})
        }


class GetAuthUserId(Resource):
    @jwt_required
    def get(self):
        return {
            'user_id': get_jwt_identity(),
        }


class GetAuthUserRole(Resource):
    @jwt_required
    def get(self):
        return {
            'user_role': get_jwt_claims()['role'],
        }


class BlacklistToken(Resource):
    @jwt_required
    def get(self):
        jti = get_raw_jwt()['jti']
        BLACKLIST.add(jti)
        return {
            'message': 'Successfully added token to blacklist.'
        }