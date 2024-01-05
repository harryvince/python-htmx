from sqlalchemy.orm import DeclarativeBase
from flask_sqlalchemy import SQLAlchemy

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

class Test(db.Model):
    __tablename__ = "Test"

    id = db.Column(db.Integer, primary_key=True)
    sample = db.Column(db.String(60), nullable=False)

    def __init__(self, sample):
        self.sample = sample

class AnotherTest(db.Model):
    __tablename__ = "AnotherTest"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    test_id = db.Column(db.Integer, db.ForeignKey("Test.id"), nullable=False)

    test = db.relationship("Test", foreign_keys=[test_id])
