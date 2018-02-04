from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, Length

class LoginForm(FlaskForm):
	username = StringField('username', validators=[InputRequired(), Length(min=4, max=45)])
	password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
	submit = SubmitField('submit')
		
class RegisterForm(FlaskForm):
	email = StringField('email', validators=[InputRequired(), Email(message='Invalid Email'), Length(min=4, max=45)])
	username = StringField('username', validators=[InputRequired(), Length(min=4, max=45)])
	password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
	submit = SubmitField('submit')