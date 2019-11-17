import os
from flask import (
	Blueprint, current_app, flash, render_template, redirect, request,
	send_from_directory, url_for,
)
from werkzeug.utils import secure_filename

router = Blueprint('main', __name__)

ALLOWED_FILE_EXTENSIONS = { 'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif' }

def allowed_file(filename: str) -> bool:
	return '.' in filename and \
		filename.rsplit('.', 1)[1].lower() in ALLOWED_FILE_EXTENSIONS


@router.route('/')
def index():
	return render_template('index.html')


@router.route('/upload', methods=['GET', 'POST'])
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
			file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
			return redirect(url_for('main.uploaded_file', filename=filename))

	# GET requests
	return render_template('upload.html')

@router.route('/uploads/<filename>')
def uploaded_file(filename):
	return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)

