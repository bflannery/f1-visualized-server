from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import DateTime, BigInteger
from sqlalchemy.sql.expression import text

from db import DeclarativeBase


class DBBaseModel(DeclarativeBase):
    __abstract__ = True
    id = Column(BigInteger, nullable=False, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, nullable=False, server_default=text("now()"))
    updated_at = Column(DateTime, nullable=False, server_default=text("now()"))
