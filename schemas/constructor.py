from typing import Optional

from schemas import BaseSchema, TimeAwareDateTime


class ConstructorSchema(BaseSchema):
    id: int
    name: str
    reference: str
    nationality: str
    wiki_url: str

    class Config:
        from_attributes = True


class ConstructorRaceSchema(BaseSchema):
    id: int
    name: str
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

    class Config:
        from_attributes = True


class ConstructorResultSchema(BaseSchema):
    id: int
    constructor: ConstructorSchema
    race: ConstructorRaceSchema
    points: int

    class Config:
        from_attributes = True
