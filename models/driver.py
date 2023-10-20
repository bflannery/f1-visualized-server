from models import DBBaseModel
from sqlalchemy import Column, Text, Integer


class DriverModel(DBBaseModel):
    __tablename__ = "driver"
    reference = Column(Text, nullable=False, unique=True, index=True)
    forename = Column(Text, nullable=False, unique=False)
    surename = Column(Text, nullable=False, unique=False)
    dob = Column(Text, nullable=False, unique=False)
    nationality = Column(Text, nullable=False, unique=False)
    code = Column(Text, nullable=True, unique=False)
    number = Column(Integer, nullable=True, unique=False)
    wiki_url = Column(Text, nullable=True, unique=False)

