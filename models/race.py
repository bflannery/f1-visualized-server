from models import DBBaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Text, Integer, DateTime, ForeignKey


class RaceStatusModel(DBBaseModel):
    __tablename__ = "race_status"
    name = Column(Text, nullable=False, unique=True)

    race_results = relationship("RaceResultModel", back_populates="race_status", lazy=True)
    sprint_results = relationship("SprintResultModel", back_populates="race_status", lazy=True)


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

    # Parents
    season = relationship("SeasonModel", back_populates="races", lazy=True)
    circuit = relationship("CircuitModel", back_populates="races", lazy=True)

    # Children
    race_results = relationship("RaceResultModel", back_populates="races", lazy=True)
    sprint_results = relationship("SprintResultModel", back_populates="races", lazy=True)
    constructor_standings = relationship("ConstructorStandingModel", back_populates="races", lazy=True)
    constructor_results = relationship("ConstructorResultModel", back_populates="races", lazy=True)
    driver_standings = relationship("DriverStandingModel", back_populates="races", lazy=True)
    lap_times = relationship("LapTimeModel", back_populates="races", lazy=True)
    pit_stops = relationship("PitStopModel", back_populates="races", lazy=True)
    qualifyings = relationship("QualifyingModel", back_populates="races", lazy=True)


class LapTimeModel(DBBaseModel):
    __tablename__ = "lap_time"
    race_id = Column(Integer, ForeignKey("race.id"), nullable=False)
    driver_id = Column(Integer, ForeignKey("driver.id"), nullable=False)
    lap = Column(Integer, nullable=False, unique=False)
    position = Column(Integer, nullable=False, unique=False)
    time = Column(Text, nullable=False, unique=False)
    time_ms = Column(Integer, nullable=False, unique=False)

    races = relationship("RaceModel", back_populates="lap_times", lazy=True)
    drivers = relationship("DriverModel", back_populates="lap_times", lazy=True)


class PitStopModel(DBBaseModel):
    __tablename__ = "pit_stop"
    race_id = Column(Integer, ForeignKey("race.id"), nullable=False)
    driver_id = Column(Integer, ForeignKey("driver.id"), nullable=False)
    lap = Column(Integer, nullable=False, unique=False)
    stop = Column(Integer, nullable=False, unique=False)
    time_of_day = Column(Text, nullable=False, unique=False)
    duration = Column(Text, nullable=False, unique=False)
    duration_ms = Column(Integer, nullable=False, unique=False)

    races = relationship("RaceModel", back_populates="pit_stops", lazy=True)
    drivers = relationship("DriverModel", back_populates="pit_stops", lazy=True)


class QualifyingModel(DBBaseModel):
    __tablename__ = "qualifying"
    race_id = Column(Integer, ForeignKey("race.id"), nullable=False)
    driver_id = Column(Integer, ForeignKey("driver.id"), nullable=False)
    constructor_id = Column(Integer, ForeignKey("constructor.id"), nullable=False)
    position = Column(Integer, nullable=False, unique=False)
    q1_time = Column(Text, nullable=True, unique=False)
    q1_time_ms = Column(Integer, nullable=True, unique=False)
    q2_time = Column(Text, nullable=True, unique=False)
    q2_time_ms = Column(Integer, nullable=True, unique=False)
    q3_time = Column(Text, nullable=True, unique=False)
    q3_time_ms = Column(Integer, nullable=True, unique=False)

    races = relationship("RaceModel", back_populates="qualifyings", lazy=True)
    drivers = relationship("DriverModel", back_populates="qualifyings", lazy=True)
    constructors = relationship("ConstructorModel", back_populates="qualifyings", lazy=True)


class RaceResultModel(DBBaseModel):
    __tablename__ = "race_result"
    race_id = Column(Integer, ForeignKey("race.id"), nullable=False)
    driver_id = Column(Integer, ForeignKey("driver.id"), nullable=False)
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
    fastest_lap_time_ms = Column(Integer, nullable=True, unique=False)
    fastest_lap_speed = Column(Text, nullable=True, unique=False)

    races = relationship("RaceModel", back_populates="race_results", lazy=True)
    drivers = relationship("DriverModel", back_populates="race_results", lazy=True)
    constructors = relationship("ConstructorModel", back_populates="race_results", lazy=True)
    race_status = relationship("RaceStatusModel", back_populates="race_results", lazy=True)


class SprintResultModel(DBBaseModel):
    __tablename__ = "sprint_result"
    race_id = Column(Integer, ForeignKey("race.id"), nullable=False)
    driver_id = Column(Integer, ForeignKey("driver.id"), nullable=False)
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

    races = relationship("RaceModel", back_populates="sprint_results", lazy=True)
    drivers = relationship("DriverModel", back_populates="sprint_results", lazy=True)
    constructors = relationship("ConstructorModel", back_populates="sprint_results", lazy=True)
    race_status = relationship("RaceStatusModel", back_populates="sprint_results", lazy=True)
