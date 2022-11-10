from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this is the key'

from . import routes
