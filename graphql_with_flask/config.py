import os
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DATABASE_URI = 'sqlite:///db.sqlite3'
DATABASE_TEST_URI = 'sqlite:///db.test.sqlite3'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from tasks.models import Task
from users.models import User