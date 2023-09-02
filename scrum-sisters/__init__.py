import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env

# Flask instance
app = Flask(__name__)
# App configuration variables
app.config["SECRET_KEY"]
app.config["SQLALCHEMY_DATABASE_URI"]

db = SQLAlchemy(app)

from scrumsisters import routes  # noqa
