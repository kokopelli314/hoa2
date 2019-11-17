from hoa.app import bcrypt, login_manager
from hoa.models import User


@login_manager.user_loader
def user_loader(user_id: int) -> User:
	return User.query.get(user_id)

def set_password(user: User, password: str):
	user.password_hash = bcrypt.generate_password_hash(password)
	user.save()

def check_password(user: User, password: str) -> bool:
	return bcrypt.check_password_hash(user.password_hash, password)
