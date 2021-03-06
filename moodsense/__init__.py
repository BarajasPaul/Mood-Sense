from flask import Flask
from flask_httpauth import HTTPBasicAuth
from flask_mongoengine import MongoEngine


# Initialize application
app = Flask(__name__)
auth = HTTPBasicAuth()

app.config['MONGODB_SETTINGS'] = {'db': 'Users'}
app.config['SECRET_KEY'] = 'YOUR_PASSPHRASE'
db = MongoEngine(app)

from moodsense import views
