from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db import get_db
from schemas import SeasonSchema
from services import season as season_service

seasons_router = APIRouter()


@seasons_router.get(
    "/{year}",
    summary="Get season by year",
    response_model=SeasonSchema
)
def get_season_by_year(year: str, db: Session = Depends(get_db)):
    db_season = season_service.get_season_by_year(db, year=year)
    import pydevd_pycharm
    pydevd_pycharm.settrace('brians-personal-mac.local', port=12345, stdoutToServer=True, stderrToServer=True)

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
