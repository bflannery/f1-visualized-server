from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db import get_db
from schemas import SeasonSchema
from services import season as season_service

seasons_router = APIRouter()


# @seasons_router.get(
#     "/{season_id}",
#     summary="Get season by id",
#     response_model=SeasonSchema
# )
# def get_season_by_id(season_id: int, db: Session = Depends(get_db)):
#     db_season = season_service.get_season_by_id(db, id=season_id)
#     if db_season is None:
#         raise HTTPException(status_code=404, detail=f"Season #{season_id} not found")
#     return db_season


@seasons_router.get(
    "/{year}",
    summary="Get season by year",
    response_model=SeasonSchema
)
def get_season_by_year(year: str, db: Session = Depends(get_db)):
    db_season = season_service.get_season_by_year(db, year=year)
    if db_season is None:
        raise HTTPException(status_code=404, detail=f"Season year '{year}' not found")
    return db_season


@seasons_router.get(
    "",
    summary="Get all seasons",
    response_model=list[SeasonSchema]
)
def get_all_seasons(db: Session = Depends(get_db)):
    all_db_seasons = season_service.get_all_seasons(db)
    return all_db_seasons
