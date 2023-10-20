from schemas import BaseSchema


class SeasonSchema(BaseSchema):
    id: int
    year: str
    wiki_url: str

    class Config:
        from_attributes = True
