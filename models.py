from sqlalchemy.orm import DeclarativeBase
from flask_sqlalchemy import SQLAlchemy

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

class Test(db.Model):
    __tablename__ = "Test"

    id = db.Column(db.Integer, primary_key=True)
    sample = db.Column(db.String(60), nullable=False)
