import os
from flask import (
	abort, Blueprint, current_app, flash, render_template, redirect, request,
	url_for,
)
from flask_login import current_user, login_user

from hoa.auth import check_password
from hoa.models import User
from hoa.forms import LoginForm

router = Blueprint('auth', __name__)


@router.route('/login', methods=['GET', 'POST'])
def login():
	# if user is already logged in, send to main page
	if current_user.is_authenticated:
		return redirect(url_for('index'))

	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is None or not check_password(user, form.password.data):
			flash('Invalid username or password')
			return redirect(url_for('auth.login'))

		login_user(user)

		next = request.args.get('next')
		if not is_safe_url(next):
			return abort(400)

		return redirect(next or url_for('index'))

	return render_template('login.html', form=form)
