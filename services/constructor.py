from sqlalchemy.orm import Session

from models import ConstructorModel, ConstructorResultModel


## Constructor
def get_constructor_by_id(db: Session, id: int) -> ConstructorModel:
    return db.query(ConstructorModel).filter(ConstructorModel.id == id).first()


def get_constructor_by_name(db: Session, name: str) -> ConstructorModel:
    return db.query(ConstructorModel).filter(ConstructorModel.name == name).first()


def get_constructor_by_reference(db: Session, reference: str) -> ConstructorModel:
    return db.query(ConstructorModel).filter(ConstructorModel.reference == reference).first()


def get_constructors_by_nationality(db: Session, nationality: str) -> ConstructorModel:
    return db.query(ConstructorModel).filter(ConstructorModel.nationality == nationality).all()


def get_all_constructors(db: Session, offset: int = 0, page_count: int = 5) -> list[ConstructorModel]:
    return db.query(ConstructorModel).offset(offset).limit(page_count + 1).all()


## Constructor Results
def get_constructor_result_by_id(db: Session, id: int) -> ConstructorResultModel:
    return db.query(ConstructorResultModel).filter(ConstructorResultModel.id == id).first()


def get_constructor_results_by_constructor_id(db: Session, constructor_id: int) -> list[ConstructorResultModel]:
    return db.query(ConstructorResultModel).filter(ConstructorResultModel.constructor_id == constructor_id).all()


def get_all_constructors_results(db: Session, page: int = 0, page_count: int = 50) -> list[ConstructorResultModel]:
    return db.query(ConstructorResultModel).offset(page).limit(page_count + 1).all()
