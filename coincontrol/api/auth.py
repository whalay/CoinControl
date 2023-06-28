from flask_httpauth import HTTPBasicAuth
from flask_restful import Api, Resource, url_for
from .decorators import monitor
from flask import Blueprint


api_auth = Blueprint("api_auth", __name__)
api = Api(api_auth, prefix="/api/v1")



auth = HTTPBasicAuth()


class Register(Resource):
    response = {"status": 400, "message": "User not created"}

    @monitor
    def post(self):
        # app login written here

        self.response["status"] = 201
        self.response["message"] = "User created sucessfully"
        return self.response, 201


api.add_resource(Register, "/register")


class Login(Resource):
    response = {"status": 400}

    @monitor
    def post(self):
        # app login written here
        pass


api.add_resource(Login, "/login")


class LoginOut(Resource):
    response = {"status": 400}

    @monitor
    def post(self):
        # app login written here
        pass


api.add_resource(LoginOut, "/logout")
