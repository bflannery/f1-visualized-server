import datetime

from sqlalchemy.orm import Session

from models import RaceModel
from schemas import RaceSchema


def get_race_by_id(db: Session, id, ) -> RaceModel:
    return db.query(RaceModel).filter(RaceModel.id == id).first()


def get_races_by_name(db: Session, name: str) -> RaceModel:
    return db.query(RaceModel).filter(RaceModel.name == name).all()


def get_all_races(db: Session) -> list[RaceModel]:
    return db.query(RaceModel).all()


def create_race(db: Session, race: RaceSchema) -> RaceModel:
    fp1_date = datetime.datetime(race.fp1_date).utcnow() if race.fp1_date else None
    fp2_date = datetime.datetime(race.fp2_date).utcnow() if race.fp2_date else None
    fp3_date = datetime.datetime(race.fp3_date).utcnow() if race.fp3_date else None
    qualifying_date = datetime.datetime(race.qualifying_date).utcnow() if race.qualifying_date else None
    sprint_date = datetime.datetime(race.sprint_date).utcnow() if race.sprint_date else None
    db_user = RaceModel(
        id=race.id,
        name=race.name,
        season_id=race.season_id,
        circuit_id=race.circuit_id,
        round=race.round,
        date=race.date,
        fp1_date=fp1_date,
        fp2_date=fp2_date,
        fp3_date=fp3_date,
        qualifying_date=qualifying_date,
        sprint_date=sprint_date,
        wiki_url=race.wiki_url,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
