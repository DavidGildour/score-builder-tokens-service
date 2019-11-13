from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from resources.token import GetToken, GetAuthUserId, GetAuthUserRole, BlacklistToken

from blacklist import BLACKLIST

app = Flask(__name__)

app.config.from_object('config.DevelopmentConfig')

api = Api(app)
jwt = JWTManager(app)

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    return decrypted_token['jti'] in BLACKLIST

api.add_resource(GetToken, '/token')
api.add_resource(GetAuthUserId, '/user_id')
api.add_resource(GetAuthUserRole, '/user_role')
api.add_resource(BlacklistToken, '/blacklist')
