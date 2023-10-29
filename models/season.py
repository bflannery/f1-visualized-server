from sqlalchemy.orm import relationship

from models import DBBaseModel
from sqlalchemy import Column, Text


class SeasonModel(DBBaseModel):
    __tablename__ = "season"
    year = Column(Text, nullable=False, unique=True, index=True)
    wiki_url = Column(Text, nullable=True, unique=False)

    races = relationship("RaceModel", back_populates="season")
