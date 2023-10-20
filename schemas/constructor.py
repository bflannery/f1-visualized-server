from schemas import BaseSchema


class ConstructorSchema(BaseSchema):
    id: int
    name: str
    reference: str
    nationality: str
    wiki_url: str

    class Config:
        from_attributes = True

