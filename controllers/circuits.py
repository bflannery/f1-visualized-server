from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db import get_db
from schemas import CircuitSchema
from services import circuit as circuit_service

circuits_router = APIRouter()


@circuits_router.get(
    "/{circuit_id}",
    summary="Get circuit by id",
    response_model=CircuitSchema
)
def get_circuit_by_id(circuit_id: int, db: Session = Depends(get_db)):
    db_circuit = circuit_service.get_circuit_by_id(db, id=circuit_id)
    if db_circuit is None:
        raise HTTPException(status_code=404, detail=f"Driver #{circuit_id} not found")
    return db_circuit


@circuits_router.get(
    "/reference/{circuit_reference}",
    summary="Get circuit by reference name",
    response_model=CircuitSchema
)
def get_circuit_by_reference(circuit_reference: str, db: Session = Depends(get_db)):
    db_circuit = circuit_service.get_circuit_by_reference(db, reference=circuit_reference)
    if db_circuit is None:
        raise HTTPException(status_code=404, detail=f"Driver reference '{circuit_reference}' not found")
    return db_circuit


@circuits_router.get(
    "/country/{circuit_country}",
    summary="Get circuits by country",
    response_model=CircuitSchema
)
def get_circuits_by_country(circuit_country: str, db: Session = Depends(get_db)):
    db_circuits = circuit_service.get_circuits_by_country(
        db,
        country=circuit_country
    )
    if db_circuits is None:
        raise HTTPException(status_code=404,
                            detail=f"Circuits for country '{circuit_country}' not found")
    return db_circuits


@circuits_router.get(
    "",
    summary="Get all circuits",
    response_model=list[CircuitSchema]
)
def get_all_circuits(db: Session = Depends(get_db)):
    all_db_circuits = circuit_service.get_all_circuits(db)
    return all_db_circuits
