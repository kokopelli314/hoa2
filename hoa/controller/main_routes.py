from hoa import documents

from flask import (
	Blueprint, current_app, flash, render_template, redirect, request,
	send_from_directory, url_for,
)
from flask_login import login_required


router = Blueprint('main', __name__)


@router.route('/')
@login_required
def index():
	return render_template('index.html')


@router.route('/upload', methods=['GET', 'POST'])
@login_required
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

		uploaded_filename = documents.upload_file(file)
		return redirect(url_for('main.uploaded_file', filename=uploaded_filename))

	# GET requests
	return render_template('upload.html')

@router.route('/uploads/<filename>')
@login_required
def uploaded_file(filename):
	return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)

@router.route('/documents')
@login_required
def documents_list():
	"""
	Lists documents available to the user.
	"""
	return render_template('documents.html')

