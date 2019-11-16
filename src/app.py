import os
from dotenv import load_dotenv

from flask import (
	Flask, flash, request, redirect, render_template, send_from_directory,
	url_for,
)
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from werkzeug.utils import secure_filename


load_dotenv()

ALLOWED_EXTENSIONS = { 'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif' }

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.getenv('DOCUMENT_UPLOAD_FOLDER')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.getenv('SECRET_KEY')

db = SQLAlchemy(app)
migrate = Migrate(app, db)



def allowed_file(filename: str) -> bool:
	return '.' in filename and \
		filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def hello():
	return 'Hello!!!!'

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
	"""
	Upload documents to the system.

	Administrators (or board members?) only.
	"""
	if request.method == 'POST':
		# validations
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)

		file = request.files['file']
		if file.filename == '':
			flash('No selected file')
			return redirect(request.url)

		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return redirect(url_for('uploaded_file', filename=filename))

	# GET requests
	return render_template('upload.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
	return send_from_directory(app.config['UPLOAD_FOLDER'], filename)



