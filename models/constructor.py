from models import DBBaseModel
from sqlalchemy import Column, Text


class ConstructorModel(DBBaseModel):
    __tablename__ = "constructor"
    reference = Column(Text, nullable=False, unique=True, index=True)
    name = Column(Text, nullable=False, unique=True, index=True)
    nationality = Column(Text, nullable=False, unique=False)
    wiki_url = Column(Text, nullable=True, unique=False)
