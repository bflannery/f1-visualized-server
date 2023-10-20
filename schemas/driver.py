from schemas import BaseSchema


class DriverSchema(BaseSchema):
    id: int
    reference: str
    forename: str
    surename: str
    dob: str
    nationality: str
    code: str
    number: int
    wiki_url: str

    class Config:
        from_attributes = True

