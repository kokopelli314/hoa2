"""
Functions to get and upload documents.
"""
import os
from flask import current_app
from werkzeug.utils import secure_filename

ALLOWED_FILE_EXTENSIONS = { 'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif' }

def allowed_file(filename: str) -> bool:
	return '.' in filename and \
		filename.rsplit('.', 1)[1].lower() in ALLOWED_FILE_EXTENSIONS

def upload_file(file) -> str:
	"""
	Returns safe uploaded file name.
	"""
	if not allowed_file(file.filename):
		raise ValueError(f'File does not have an allowed extension: "{file.filename}"')

	filename = secure_filename(file.filename)
	file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

	return filename
