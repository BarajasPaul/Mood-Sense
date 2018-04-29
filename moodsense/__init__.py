from flask import Flask


# Initialize application
app = Flask(__name__)

from moodsense import views
