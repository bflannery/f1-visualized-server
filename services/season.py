from sqlalchemy.orm import Session

from models import SeasonModel


def get_season_by_id(db: Session, id: int) -> SeasonModel:
    return db.query(SeasonModel).filter(SeasonModel.id == id).first()


def get_season_by_year(db: Session, year: str) -> SeasonModel:
    return db.query(SeasonModel).filter(SeasonModel.year == year).first()


def get_all_seasons(db: Session) -> list[SeasonModel]:
    return db.query(SeasonModel).all()
