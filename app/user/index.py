from flask.ext.restful import Resource, Api, fields, marshal_with, abort, reqparse

from models.user import User
import datetime


class User(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("email", type=str, required=True,
            help="Email is required")
        self.parser.add_argument("pass", type=str, required=True,
            help="Password is required")
        self.parser.add_argument("id", type=str, help="User id")
        self.parser.add_argument("image")
        self.args = self.parser.parse_args()

    # @marshal_with(User.format())
    def get(self, id):
        pass

    def post(self):
        pass

    def put(self, id):
        pass

    def delete(self,id):
        pass
