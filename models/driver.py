from sqlalchemy.orm import relationship

from models import DBBaseModel
from sqlalchemy import Column, Text, Integer, ForeignKey


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

    lap_times = relationship("LapTimeModel", back_populates="drivers", lazy=True)
    pit_stops = relationship("PitStopModel", back_populates="drivers", lazy=True)
    qualifyings = relationship("QualifyingModel", back_populates="drivers", lazy=True)
    race_results = relationship("RaceResultModel", back_populates="drivers", lazy=True)
    sprint_results = relationship("SprintResultModel", back_populates="drivers", lazy=True)
    driver_standings = relationship("DriverStandingModel", back_populates="drivers", lazy=True)


class DriverStandingModel(DBBaseModel):
    __tablename__ = "driver_standing"
    race_id = Column(Integer, ForeignKey("race.id"), nullable=False)
    driver_id = Column(Integer, ForeignKey("driver.id"), nullable=False)
    points_total = Column(Integer, nullable=False, unique=False)
    position = Column(Integer, nullable=False, unique=False)
    wins = Column(Integer, nullable=False, unique=False)

    races = relationship("RaceModel", back_populates="driver_standings", lazy=True)
    drivers = relationship("DriverModel", back_populates="driver_standings", lazy=True)
