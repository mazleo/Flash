
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(15), unique=True)
    password = db.Column(db.String(20))
    logged_in = db.Column(db.Boolean)
    chat_msgs = db.relationship('Message', backref='user', lazy='dynamic')

    def __init__(self, email, username, password, logged_in):
        self.email = email
        self.username = username
        self.password = password
        self.logged_in = logged_in

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_code = db.Column(db.String)
    chat_msg = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, room_code, chat_msg, user):
        self.room_code = room_code
        self.chat_msg = chat_msg
        self.user_id = user.id
