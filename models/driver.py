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


class DriverStandingModel(DBBaseModel):
    __tablename__ = "driver_standing"
    race_id = Column(Integer, ForeignKey("race.id"), nullable=False)
    driver_id = Column(Integer, ForeignKey("driver.id"), nullable=False)
    points_total = Column(Integer, nullable=False, unique=False)
    position = Column(Integer, nullable=False, unique=False)
    wins = Column(Integer, nullable=False, unique=False)

    race = relationship("RaceModel")
    constructor = relationship("DriverModel")
