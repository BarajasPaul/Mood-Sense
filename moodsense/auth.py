from moodsense import app, db, auth

from flask import request, jsonify, abort



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
