
import uuid
import sys
from sqlalchemy.dialects.postgresql import ARRAY
from app import db



class User(db.Model):
    """A user."""
    id = db.Column(db.Integer, primary_key=True)

	username = db.Column(db.String(), nullable=False)
	# bcrypt hash of user's password
	password = db.Column(db.String(), nullable=False)

	first_name = db.Column(db.String(), nullable=False)
	last_name = db.Column(db.String(), nullable=False)
	email_address = db.Column(db.String(), nullable=False)

	street_address = db.Column(db.String(), nullable=True)
	unit_number = db.Column(db.String(), nullable=True)

	is_board_member = db.Column(db.Boolean(), default=False, nullable=False)
	is_admin = db.Column(db.Boolean(), default=False, nullable=False)
