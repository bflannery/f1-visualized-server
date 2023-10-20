from sqlalchemy.orm import Session

from models import RaceModel


def get_race_by_id(db: Session, id: int) -> RaceModel:
    return db.query(RaceModel).filter(RaceModel.id == id).first()


def get_races_by_name(db: Session, name: str) -> RaceModel:
    return db.query(RaceModel).filter(RaceModel.name == name).all()


def get_all_races(db: Session) -> list[RaceModel]:
    return db.query(RaceModel).all()
