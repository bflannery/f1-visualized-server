from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db import get_db
from schemas import RaceSchema
from services import race as race_service

races_router = APIRouter()


@races_router.get(
    "/{race_id}",
    summary="Get race by id",
    response_model=RaceSchema
)
def get_race_by_id(race_id: int, db: Session = Depends(get_db)):
    db_race = race_service.get_race_by_id(db, id=race_id)
    if db_race is None:
        raise HTTPException(status_code=404, detail=f"Season #{race_id} not found")
    return db_race


@races_router.get(
    "/{race_name}",
    summary="Get races by name",
    response_model=list[RaceSchema]
)
def get_races_by_name(race_name: str, db: Session = Depends(get_db)):
    db_races = race_service.get_races_by_name(db, name=race_name)
    if db_races is None:
        raise HTTPException(status_code=404, detail=f"No {race_name} races not found")
    return db_races


@races_router.get(
    "",
    summary="Get all races",
    response_model=list[RaceSchema]
)
def get_all_races(db: Session = Depends(get_db)):
    all_db_races = race_service.get_all_races(db)
    return all_db_races


@races_router.post("", summary="Create new race", response_model=RaceSchema)
def create_user(race: RaceSchema, db: Session = Depends(get_db)):
    return race_service.create_race(db=db, race=race)

