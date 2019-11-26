
import enum
import uuid
import sys
from flask_login import UserMixin
from sqlalchemy import Column, Enum, ForeignKey, Boolean, Integer, String

from hoa.app import db

class DocumentType(enum.Enum):
	meeting_notes = 'meeting_notes'
	board_internal = 'board_internal'


class User(db.Model, UserMixin):
	"""A user."""
	id = Column(db.Integer, primary_key=True)

	username = Column(String(), nullable=False)
	# bcrypt hash of user's password
	password_hash = Column(String(), nullable=False)

	first_name = Column(String(), default='', nullable=False)
	last_name = Column(String(), default='', nullable=False)
	email_address = Column(String(), nullable=False)

	street_address = Column(String(), nullable=True)
	unit_number = Column(String(), nullable=True)

	is_board_member = Column(Boolean(), default=False, nullable=False)
	is_admin = Column(Boolean(), default=False, nullable=False)


class Document(db.Model):
	"""HOA documents."""
	id = Column(Integer, primary_key=True)
	uploaded_by = Column(ForeignKey('user.id'), nullable=False)
	document_type = Column(Enum(DocumentType), nullable=True)
	# file location relative to the root document folder
	filepath = Column(String(), nullable=False)

class Comment(db.Model):
	"""
	A comment on a document or a post.
	"""
	id = Column(Integer, primary_key=True)
	author = Column(ForeignKey('user.id'), nullable=False)
	message = Column(String, nullable=False)
	document = Column(ForeignKey('document.id'), nullable=True)


# class Poll(db.Model):
# 	"""TODO"""
# 	pass
# 	# id = Column(Integer, primary_key=True)

# class Vote(db.Model):
# 	"""TODO"""
# 	pass
