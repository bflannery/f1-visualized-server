from datetime import datetime, timezone
from typing import Generic, TypeVar, Annotated

from pydantic import BaseModel, Field, PlainSerializer, field_validator

TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"

TimeAwareDateTime = Annotated[
    datetime, PlainSerializer(lambda dt: dt.astimezone(timezone.utc).strftime(TIME_FORMAT))
]

DataType = TypeVar("DataType")


class Result(BaseModel, Generic[DataType]):
    result: DataType


class BaseSchema(BaseModel):
    created_at: TimeAwareDateTime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: TimeAwareDateTime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator("created_at", "updated_at")
    @classmethod
    def utc_times(cls, v):
        if tzname := v.tzname():
            assert tzname == str(timezone.utc), "TZ is not UTC"
        return v
