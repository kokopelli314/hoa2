import os
from flask import (
	abort, Blueprint, current_app, flash, render_template,
	redirect, request, url_for,
)
from flask_login import current_user, login_required, login_user, logout_user

from hoa.app import db, login_manager
from hoa.auth import check_password, get_user_by_username, create_user
from hoa.models import User
from hoa.forms import LoginForm, RegistrationForm

router = Blueprint('auth', __name__)


@router.route('/login', methods=['GET', 'POST'])
def login():
	# if user is already logged in, send to main page
	if current_user.is_authenticated:
		return redirect(url_for('main.index'))

	form = LoginForm()
	if form.validate_on_submit():
		user = get_user_by_username(form.username.data)
		if user is None or not check_password(user, form.password.data):
			flash('Invalid username or password')
			return redirect(url_for('auth.login'))

		login_user(user)

		next = request.args.get('next')
		return redirect(next or url_for('main.index'))

	return render_template('login.html', form=form)

login_manager.login_view = 'auth.login'

@router.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('auth.login'))

@router.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('main.index'))

	form = RegistrationForm()
	if form.validate_on_submit():
		user = create_user(form.username.data, form.password.data, form.email_address.data)
		db.session.add(user)
		db.session.commit()
		flash('Congratulations, you are now a registered user!')
		return redirect(url_for('auth.login'))

	return render_template('register.html', title='Register', form=form)
















