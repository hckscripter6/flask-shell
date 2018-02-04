from config import db, app
from flask_login import UserMixin

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(25))
	username = db.Column(db.String(50), unique=True)
	password = db.Column(db.String(80))