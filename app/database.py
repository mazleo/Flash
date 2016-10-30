
from app import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)
class users(db.Model):
    email = db.Column(db.String(50))
    username = db.Column(db.String(15))
    password = db.Column(db.String(20))

def __init__(self, email, username, password):
    self.email = email
    self.username = username
    self.password = password
