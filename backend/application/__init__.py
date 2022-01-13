from flask import Flask
from flask_cors import CORS
from . import main
from .api_test import test
import os

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__)
CORS(app)
app.secret_key = 'cky0935'



app.register_blueprint(main.main)
app.register_blueprint(test.test)

