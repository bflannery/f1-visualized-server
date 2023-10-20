from sqlalchemy.orm import Session

from models import ConstructorModel


def get_constructor_by_id(db: Session, id: int) -> ConstructorModel:
    return db.query(ConstructorModel).filter(ConstructorModel.id == id).first()


def get_constructor_by_name(db: Session, name: str) -> ConstructorModel:
    return db.query(ConstructorModel).filter(ConstructorModel.name == name).first()


def get_constructor_by_reference(db: Session, reference: str) -> ConstructorModel:
    return db.query(ConstructorModel).filter(ConstructorModel.reference == reference).first()


def get_constructors_by_nationality(db: Session, nationality: str) -> ConstructorModel:
    return db.query(ConstructorModel).filter(ConstructorModel.nationality == nationality).all()


def get_all_constructors(db: Session) -> list[ConstructorModel]:
    return db.query(ConstructorModel).all()
