from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db import get_db
from schemas import DriverSchema
from services import driver as driver_service

drivers_router = APIRouter()


@drivers_router.get(
    "/{driver_id}",
    summary="Get driver by id",
    response_model=DriverSchema
)
def get_driver_by_id(driver_id: int, db: Session = Depends(get_db)):
    db_driver = driver_service.get_driver_by_id(db, id=driver_id)
    if db_driver is None:
        raise HTTPException(status_code=404, detail=f"Driver #{driver_id} not found")
    return db_driver


@drivers_router.get(
    "/reference/{driver_reference}",
    summary="Get driver by reference name",
    response_model=DriverSchema
)
def get_driver_by_reference(driver_reference: str, db: Session = Depends(get_db)):
    db_driver = driver_service.get_driver_by_reference(db, reference=driver_reference)
    if db_driver is None:
        raise HTTPException(status_code=404, detail=f"Driver reference '{driver_reference}' not found")
    return db_driver


@drivers_router.get(
    "/nationality/{driver_nationality}",
    summary="Get drivers by nationality",
    response_model=DriverSchema
)
def get_drivers_by_nationality(driver_nationality: str, db: Session = Depends(get_db)):
    db_drivers = driver_service.get_drivers_by_nationality(
        db,
        nationality=driver_nationality
    )
    if db_drivers is None:
        raise HTTPException(status_code=404,
                            detail=f"Drivers for nationality'{driver_nationality}' not found")
    return db_drivers


@drivers_router.get(
    "",
    summary="Get all drivers",
    response_model=list[DriverSchema]
)
def get_all_drivers(db: Session = Depends(get_db)):
    all_db_drivers = driver_service.get_all_drivers(db)
    return all_db_drivers
