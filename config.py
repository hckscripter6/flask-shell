from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://lefdbeqiysaorl:1f8408a1445e1b482ba5dd0900e401202269d6ec7f6e4168871e0b6a1fb60fa1@ec2-54-83-203-198.compute-1.amazonaws.com:5432/d8n1smr8bnouet'

app.config['SECRET_KEY'] = '7"#~L?y78hWq%~NV'


