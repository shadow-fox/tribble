from flask import Flask
from flask.ext import restful
from user.index import User
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
api = restful.Api(app)

api.add_resource(User, "/user/<string:id>", "/user")
