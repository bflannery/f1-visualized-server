from sqlalchemy.orm import relationship
from sqlalchemy import Column, Text, Integer
from models import DBBaseModel


class CircuitModel(DBBaseModel):
    __tablename__ = "circuit"
    reference = Column(Text, nullable=False, unique=True, index=True)
    name = Column(Text, nullable=False, unique=True, index=True)
    location = Column(Text, nullable=False, unique=False)
    country = Column(Text, nullable=False, unique=False)
    latitude = Column(Text, nullable=False, unique=False)
    longitude = Column(Text, nullable=False, unique=False)
    wiki_url = Column(Text, nullable=True, unique=False)

    races = relationship("RaceModel", back_populates="circuit")
