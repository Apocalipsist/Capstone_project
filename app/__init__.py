# Import flask
from flask import Flask
# Import SQLalchemy and Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# Import login management
from flask_login import LoginManager
from config import Config

app = Flask(__name__)

# Add a secret_Key to app config
app.config.from_object(Config)

db = SQLAlchemy(app)

migrate = Migrate(app, db, render_as_batch=True)

# Allow login abilities
login = LoginManager(app)
login.login_view = 'login'
login.login_message_category = 'danger'

from . import routes, models