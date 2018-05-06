from datetime import datetime
from passlib.hash import sha256_crypt
from app import db

class User(db.Document):
    name = db.StringField(max_length=80, unique=True)
    password = db.StringField(max_length=256)
    create_date = db.DateTimeField(default=datetime.now)
    last_access = db.DateTimeField(default=datetime.now)
    Attempts = db.IntField(rounding='ROUND_HALF_UP')

    def hash_password(self, password):
        self.password = sha256_crypt.encrypt(password)

    def verify_password(self, password):
        return  sha256_crypt.verify(password, self.password)


class Mood(db.Document):
    id = db.ObjectidField()
    location = db.DictField(field=['address', 'place', 'gps'])
    date = db.DateTimeField(default=datetime.now)
    expression =  db.StringField(max_length=32)
