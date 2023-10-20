from models import DBBaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Text, Integer, DateTime, ForeignKey


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
