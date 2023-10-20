from sqlalchemy.orm import Session

from models import CircuitModel


def get_circuit_by_id(db: Session, id: int) -> CircuitModel:
    return db.query(CircuitModel).filter(CircuitModel.id == id).first()


def get_circuit_by_reference(db: Session, reference: str) -> CircuitModel:
    return db.query(CircuitModel).filter(CircuitModel.reference == reference).first()


def get_circuits_by_country(db: Session, country: str) -> CircuitModel:
    return db.query(CircuitModel).filter(CircuitModel.country == country).all()


def get_all_circuits(db: Session) -> list[CircuitModel]:
    return db.query(CircuitModel).all()
