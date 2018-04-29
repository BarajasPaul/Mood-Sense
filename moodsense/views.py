from moodsense import app
from moodsense.auth import auth

@app.route('/hello')
@auth.login_required
def index():
    return "Hello, World!"
