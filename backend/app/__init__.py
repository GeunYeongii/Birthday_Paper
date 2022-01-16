from flask import Flask
from . import main
from .controller.letterController import letter
from .controller.joinController import join
from .api_test import test
import os
from .init_app import *



os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = init_app(app)

app.register_blueprint(main.main)
app.register_blueprint(test.test)
app.register_blueprint(letter)
app.register_blueprint(join)


