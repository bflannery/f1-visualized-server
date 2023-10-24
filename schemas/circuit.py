from typing import Optional

from schemas import BaseSchema, TimeAwareDateTime


class CircuitSchema(BaseSchema):
    id: int
    reference: str
    name: str
    location: str
    country: str
    latitude: int
    longitude: int
    wiki_url: str

    class Config:
        from_attributes = True


class CircuitRaceSchema(BaseSchema):
    id: int
    season_id: int
    circuit_id: int
    round: int
    date: TimeAwareDateTime
    fp1_date: Optional[TimeAwareDateTime]
    fp2_date: Optional[TimeAwareDateTime]
    fp3_date: Optional[TimeAwareDateTime]
    qualifying_date: Optional[TimeAwareDateTime]
    sprint_date: Optional[TimeAwareDateTime]
    wiki_url: str


class CircuitRacesSchema(BaseSchema):
    id: int
    reference: str
    name: str
    location: str
    country: str
    latitude: int
    longitude: int
    wiki_url: str
    races: list[CircuitRaceSchema]
