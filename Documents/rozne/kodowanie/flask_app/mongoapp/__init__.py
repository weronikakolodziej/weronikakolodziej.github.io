from flask import Flask
from .extensions import mongo
from .main.routes import main

#app = Flask(__name__)
user = 0
pwd = 0
dbname = 0

mongo_string = 'mongodb+srv://weronikako:<password>@cluster0.x5xn1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'


def create_app():
    app = Flask(__name__)
    app.config['MONGO_URI'] = mongo_string
    app.register_blueprint(main)
    return app


def users():
    return {{users}}
