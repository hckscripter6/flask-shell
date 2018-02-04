from config import app, db
from flask import render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from forms import LoginForm, RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash
from models import User

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):	
	return User.query.get(int(user_id))
	
@app.route('/', methods=["GET", "POST"])
def index():
	return render_template('index.html')
	
@app.route('/signup', methods=["GET", "POST"])
def signup():
	form = RegisterForm()
	if form.validate_on_submit():
		hashed_password = generate_password_hash(form.password.data, method='sha256')
		new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
		db.session.add(new_user)
		db.session.commit()
		return '<h1>New user has been created</h1>'
	return render_template('authentication/signup.html', form=form)
	
@app.route('/login', methods=["GET", "POST"])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user:
			if check_password_hash(user.password, form.password.data):
				login_user(user)
				return redirect(url_for('dashboard'))
	return render_template('authentication/login.html', form=form)
	
@app.route('/dashboard')
@login_required
def dashboard():
	return render_template('authentication/dashboard.html')
	
@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('index'))