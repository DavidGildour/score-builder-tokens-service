import json


def get_json_content(response) -> dict:
    """ Returns a dict-translated JSON with content of the response """
    return json.loads(response.get_data(as_text=True))