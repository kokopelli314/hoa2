import os
from dotenv import load_dotenv
import flask
from flask import (
	Flask, flash, request, redirect, render_template, send_from_directory,
	url_for,
)
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect


load_dotenv()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.getenv('DOCUMENT_UPLOAD_FOLDER')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.getenv('SECRET_KEY')

csrf = CSRFProtect(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

# Register application routes
from hoa.auth.controller import router as auth_router
from hoa.controller.main_routes import router as main_router
app.register_blueprint(auth_router)
app.register_blueprint(main_router)


