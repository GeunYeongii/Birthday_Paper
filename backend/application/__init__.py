from flask import Flask
from flask_cors import CORS
from . import main
from .controller.letterController import letter
import os

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__)
CORS(app)
app.secret_key = 'cky0935'

app.register_blueprint(main.main)
app.register_blueprint(letter)


