from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship
from sqlalchemy import String, ForeignKey
from flask_sqlalchemy import SQLAlchemy

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

class Test(Base):
    __tablename__ = "Test"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    sample: Mapped[str] = mapped_column(String(60), nullable=False)

    def __init__(self, sample):
        self.sample = sample

class AnotherTest(Base):
    __tablename__ = "AnotherTest"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(60), nullable=False)
    test_id: Mapped[int] = mapped_column(ForeignKey("Test.id"), nullable=False)
