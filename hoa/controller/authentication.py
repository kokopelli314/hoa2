from flask_login import login_user, LoginForm

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		login_user(user)
		flask.flash('Logged in Success')

		next = flask.request.args.get('next')
		if not is_safe_url(next):
			return flask.abort(400)

		return redirect(next or url_for('index'))

	return flask.render_template('login.html', form=form)
