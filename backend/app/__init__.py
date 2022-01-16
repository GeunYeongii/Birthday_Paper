from flask import Flask
from flask_cors import CORS
from . import main
from .controller.letterController import letter
from .controller.userController import user
import os
from flask_sqlalchemy import SQLAlchemy

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'd9owj3982oi8329dsh38'
# mysql://username:password@localhost/db_name'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://dave:wnrmsdud12!@localhost:3306/birthday_paper'

db = SQLAlchemy(app)




app.register_blueprint(main.main)
app.register_blueprint(letter)
app.register_blueprint(user)


