from schemas import BaseSchema


class CircuitSchema(BaseSchema):
    id: int
    reference: str
    name: str
    location: str
    country: str
    latitude: int
    longitude: int
    altitude: int
    wiki_url: str

    class Config:
        from_attributes = True
