from hoa.app import bcrypt, login_manager
from hoa.models import User

from typing import Tuple

@login_manager.user_loader
def user_loader(user_id: int) -> User:
	return User.query.get(user_id)

def get_user_by_username(username: str) -> Tuple[User, None]:
	return User.query.filter_by(username=username).first()

def create_user(username: str, password: str, email_address: str) -> User:
	password_hash = bcrypt.generate_password_hash(password).decode('utf8')
	user = User(
		username=username,
		password_hash=password_hash,
		email_address=email_address,
	)
	return user

def set_password(user: User, password: str):
	user.password_hash = bcrypt.generate_password_hash(password).decode('utf8')
	user.save()

def check_password(user: User, password: str) -> bool:
	return bcrypt.check_password_hash(user.password_hash, password)
