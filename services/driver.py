from sqlalchemy.orm import Session

from models import DriverModel


def get_driver_by_id(db: Session, id: int) -> DriverModel:
    return db.query(DriverModel).filter(DriverModel.id == id).first()


def get_driver_by_reference(db: Session, reference: str) -> DriverModel:
    return db.query(DriverModel).filter(DriverModel.reference == reference).first()


def get_drivers_by_nationality(db: Session, nationality: str) -> DriverModel:
    return db.query(DriverModel).filter(DriverModel.nationality == nationality).all()


def get_all_drivers(db: Session) -> list[DriverModel]:
    return db.query(DriverModel).all()
