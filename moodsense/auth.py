from moodsense import app, db, auth

from passlib.hash import sha256_crypt
from flask import request, jsonify, abort


class UserAuth(db.Document):
    name = db.StringField(max_length=80, unique=True)
    password = db.StringField(max_length=256)

    def hash_password(self, password):
        self.password = sha256_crypt.encrypt(password)

    def verify_password(self, password):
        return  sha256_crypt.verify(password, self.password)


@app.route("/api/users", methods = ['POST'])
def new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        abort(400)

    if UserAuth.objects(name=username):
        print("User already exists")
        abort(400)

    user = UserAuth(name = username)
    user.hash_password(password)
    user.save()


    return jsonify({ 'username': user.name, 'password': user._id})

@auth.verify_password
def verify_password(username, password):
    check_user = UserAuth.objects(name=username).first()
    if check_user and check_user.verify_password(password):
        print("Password is correct!")
        return True
    else:
        return False
