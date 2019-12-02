from flask import Flask
from config import Config
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

login = LoginManager(app)

from app import routes
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired