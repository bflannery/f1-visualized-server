from schemas import BaseSchema, TimeAwareDateTime


class RaceSchema(BaseSchema):
    id: int
    season_id: int
    circuit_id: int
    round: int
    date: TimeAwareDateTime
    fp1_date: TimeAwareDateTime
    fp2_date: TimeAwareDateTime
    fp3_date: TimeAwareDateTime
    qualifying_date: TimeAwareDateTime
    sprint_date: TimeAwareDateTime
    wiki_url: str

    class Config:
        from_attributes = True
