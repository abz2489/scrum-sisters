import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    login_required,
    logout_user,
    current_user
)
if os.path.exists("env.py"):
    import env

# Flask instance
app = Flask(__name__)
# App configuration variables
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config['SQLALCHEMY_POOL_SIZE'] = 20
app.config['SQLALCHEMY_MAX_OVERFLOW'] = 30
if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    uri = os.environ.get("DB_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Flask login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


from scrumsisters import routes  # noqa
