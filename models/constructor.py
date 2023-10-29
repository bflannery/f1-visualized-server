from sqlalchemy.orm import relationship

from models import DBBaseModel
from sqlalchemy import Column, Text, Integer, ForeignKey


class ConstructorModel(DBBaseModel):
    __tablename__ = "constructor"
    reference = Column(Text, nullable=False, unique=True, index=True)
    name = Column(Text, nullable=False, unique=True, index=True)
    nationality = Column(Text, nullable=False, unique=False)
    wiki_url = Column(Text, nullable=True, unique=False)

    qualifyings = relationship("QualifyingModel", back_populates="constructors", lazy=True)
    race_results = relationship("RaceResultModel", back_populates="constructors", lazy=True)
    sprint_results = relationship("SprintResultModel", back_populates="constructors", lazy=True)
    constructor_results = relationship("ConstructorResultModel", back_populates="constructors", lazy=True)
    constructor_standings = relationship("ConstructorStandingModel", back_populates="constructors", lazy=True)


class ConstructorResultModel(DBBaseModel):
    __tablename__ = "constructor_result"
    race_id = Column(Integer, ForeignKey("race.id"), nullable=False)
    constructor_id = Column(Integer, ForeignKey("constructor.id"), nullable=False)
    points = Column(Integer, nullable=False, unique=False)

    races = relationship("RaceModel", back_populates="constructor_results", lazy=True)
    constructors = relationship("ConstructorModel", back_populates="constructor_results", lazy=True)


class ConstructorStandingModel(DBBaseModel):
    __tablename__ = "constructor_standing"
    race_id = Column(Integer, ForeignKey("race.id"), nullable=False)
    constructor_id = Column(Integer, ForeignKey("constructor.id"), nullable=False)
    points_total = Column(Integer, nullable=False, unique=False)
    position = Column(Integer, nullable=False, unique=False)
    wins = Column(Integer, nullable=False, unique=False)

    races = relationship("RaceModel", back_populates="constructor_standings", lazy=True)
    constructors = relationship("ConstructorModel", back_populates="constructor_standings", lazy=True)
