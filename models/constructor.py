from sqlalchemy.orm import relationship

from models import DBBaseModel
from sqlalchemy import Column, Text, Integer, ForeignKey


class ConstructorModel(DBBaseModel):
    __tablename__ = "constructor"
    reference = Column(Text, nullable=False, unique=True, index=True)
    name = Column(Text, nullable=False, unique=True, index=True)
    nationality = Column(Text, nullable=False, unique=False)
    wiki_url = Column(Text, nullable=True, unique=False)


class ConstructorResultModel(DBBaseModel):
    __tablename__ = "constructor_result"
    race_id = Column(Integer, ForeignKey("race.id"), nullable=False)
    constructor_id = Column(Integer, ForeignKey("constructor.id"), nullable=False)
    points = Column(Integer, nullable=False, unique=False)
    race = relationship("RaceModel")
    constructor = relationship("ConstructorModel")


class ConstructorStandingModel(DBBaseModel):
    __tablename__ = "constructor_standing"
    race_id = Column(Integer, ForeignKey("race.id"), nullable=False)
    constructor_id = Column(Integer, ForeignKey("constructor.id"), nullable=False)
    points_total = Column(Integer, nullable=False, unique=False)
    position = Column(Integer, nullable=False, unique=False)
    wins = Column(Integer, nullable=False, unique=False)

    race = relationship("RaceModel")
    constructor = relationship("ConstructorModel")
