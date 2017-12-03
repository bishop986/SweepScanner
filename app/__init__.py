from flask import Flask
from flask_bootstrap import Bootstrap
import os

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = os.urandom(24)
app.config.from_pyfile('setting.cfg')

from app import view
