from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from application.config import config

app = Flask(__name__)
login = LoginManager(app)
login.login_view = 'login'

app.config.from_object(config)

db = SQLAlchemy(app)

from application import routes