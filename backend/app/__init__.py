from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

from .controller.letterController import letter
from .controller.userController import user
import os

app = Flask(__name__)
CORS(app)

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
app.config['SECRET_KEY'] = 'd9owj3982oi8329dsh38'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://public0917:public2423!@211.47.75.102:3306/dbpublic0917'

app.register_blueprint(letter)
app.register_blueprint(user)

jwt = JWTManager(app)
db = SQLAlchemy(app)
