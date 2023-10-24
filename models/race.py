from models import DBBaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Text, Integer, DateTime, ForeignKey


class RaceStatusModel(DBBaseModel):
    __tablename__ = "race_status"
    name = Column(Text, nullable=False, unique=True)


class RaceModel(DBBaseModel):
    __tablename__ = "race"

    season_id = Column(Integer, ForeignKey("season.id"), nullable=False)
    circuit_id = Column(Integer, ForeignKey("circuit.id"), nullable=False)
    round = Column(Integer, nullable=False, unique=False)
    name = Column(Text, nullable=False, unique=False)
    date = Column(DateTime, nullable=False, unique=False)
    fp1_date = Column(DateTime, nullable=True, unique=False)
    fp2_date = Column(DateTime, nullable=True, unique=False)
    fp3_date = Column(DateTime, nullable=True, unique=False)
    qualifying_date = Column(DateTime, nullable=True, unique=False)
    sprint_date = Column(DateTime, nullable=True, unique=False)
    wiki_url = Column(Text, nullable=True, unique=False)

    season = relationship("SeasonModel")
    circuit = relationship("CircuitModel")


class LapTimeModel(DBBaseModel):
    __tablename__ = "lap_time"
    race_id = Column(Integer, ForeignKey("race.id"), nullable=False)
    driver_id = Column(Integer, ForeignKey("driver_id.id"), nullable=False)
    lap = Column(Integer, nullable=False, unique=False)
    position = Column(Integer, nullable=False, unique=False)
    time = Column(Text, nullable=False, unique=False)
    time_ms = Column(Integer, nullable=False, unique=False)

    race = relationship("RaceModel")
    driver = relationship("DriverModel")


class PitStopModel(DBBaseModel):
    __tablename__ = "pit_stop"
    race_id = Column(Integer, ForeignKey("race.id"), nullable=False)
    driver_id = Column(Integer, ForeignKey("driver_id.id"), nullable=False)
    lap = Column(Integer, nullable=False, unique=False)
    stop = Column(Integer, nullable=False, unique=False)
    time_of_day = Column(Text, nullable=False, unique=False)
    duration = Column(Text, nullable=False, unique=False)

    race = relationship("RaceModel")
    driver = relationship("DriverModel")


class QualifyingModel(DBBaseModel):
    __tablename__ = "qualifying"
    race_id = Column(Integer, ForeignKey("race.id"), nullable=False)
    driver_id = Column(Integer, ForeignKey("driver_id.id"), nullable=False)
    constructor_id = Column(Integer, ForeignKey("constructor.id"), nullable=False)
    position = Column(Integer, nullable=False, unique=False)
    q1 = Column(Text, nullable=True, unique=False)
    q2 = Column(Text, nullable=True, unique=False)
    q3 = Column(Text, nullable=True, unique=False)

    race = relationship("RaceModel")
    driver = relationship("DriverModel")
    constructor = relationship("ConstructorModel")


class RaceResultModel(DBBaseModel):
    __tablename__ = "race_result"
    race_id = Column(Integer, ForeignKey("race.id"), nullable=False)
    driver_id = Column(Integer, ForeignKey("driver_id.id"), nullable=False)
    constructor_id = Column(Integer, ForeignKey("constructor.id"), nullable=False)
    grid = Column(Integer, nullable=False, unique=False)
    position = Column(Integer, nullable=False, unique=False)
    points = Column(Integer, nullable=False, unique=False)
    laps = Column(Integer, nullable=False, unique=False)
    rank = Column(Integer, nullable=True, unique=False)
    race_status_id = Column(Integer, ForeignKey("race_status.id"), nullable=False)
    time = Column(Text, nullable=True, unique=False)
    time_ms = Column(Integer, nullable=True, unique=False)
    fastest_lap = Column(Integer, nullable=True, unique=False)
    fastest_lap_time = Column(Text, nullable=True, unique=False)
    fastest_lap_speed = Column(Text, nullable=True, unique=False)

    race = relationship("RaceModel")
    driver = relationship("DriverModel")
    constructor = relationship("ConstructorModel")
    race_status = relationship("RaceStatusModel")


class SprintResultModel(DBBaseModel):
    __tablename__ = "sprint_result"
    race_id = Column(Integer, ForeignKey("race.id"), nullable=False)
    driver_id = Column(Integer, ForeignKey("driver_id.id"), nullable=False)
    constructor_id = Column(Integer, ForeignKey("constructor.id"), nullable=False)
    grid = Column(Integer, nullable=False, unique=False)
    position = Column(Integer, nullable=False, unique=False)
    points = Column(Integer, nullable=False, unique=False)
    laps = Column(Integer, nullable=False, unique=False)
    race_status_id = Column(Integer, ForeignKey("race_status.id"), nullable=False)
    time = Column(Text, nullable=True, unique=False)
    time_ms = Column(Integer, nullable=True, unique=False)
    fastest_lap = Column(Integer, nullable=True, unique=False)
    fastest_lap_time = Column(Text, nullable=True, unique=False)

    race = relationship("RaceModel")
    driver = relationship("DriverModel")
    constructor = relationship("ConstructorModel")
    race_status = relationship("RaceStatusModel")
