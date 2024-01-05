from flask import Flask
from flask_migrate import Migrate
from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'

Migrate(app, db)
db.init_app(app)

with app.app_context():
    db.create_all()
