from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db import get_db
from schemas import ConstructorSchema
from services import constructor as constructor_service

constructors_router = APIRouter()


@constructors_router.get(
    "/{constructor_id}",
    summary="Get constructor by id",
    response_model=ConstructorSchema
)
def get_constructor_by_id(constructor_id: int, db: Session = Depends(get_db)):
    db_constructor = constructor_service.get_constructor_by_id(db, id=constructor_id)
    if db_constructor is None:
        raise HTTPException(status_code=404, detail=f"Constructor #{constructor_id} not found")
    return db_constructor


@constructors_router.get(
    "/reference/{constructor_reference}",
    summary="Get constructor by reference name",
    response_model=ConstructorSchema
)
def get_constructor_by_reference(constructor_reference: str, db: Session = Depends(get_db)):
    db_constructor = constructor_service.get_constructor_by_reference(db, reference=constructor_reference)
    if db_constructor is None:
        raise HTTPException(status_code=404, detail=f"Constructor reference '{constructor_reference}' not found")
    return db_constructor


@constructors_router.get(
    "/nationality/{constructor_nationality}",
    summary="Get constructors by nationality",
    response_model=ConstructorSchema
)
def get_constructor_by_name(constructor_nationality: str, db: Session = Depends(get_db)):
    db_constructors = constructor_service.get_constructors_by_nationality(
        db,
        nationality=constructor_nationality
    )
    if db_constructors is None:
        raise HTTPException(status_code=404,
                            detail=f"Constructors for nationality'{constructor_nationality}' not found")
    return db_constructors


@constructors_router.get(
    "",
    summary="Get all constructors",
    response_model=list[ConstructorSchema]
)
def get_all_constructors(offset: int = 0, page_count: int = 50, db: Session = Depends(get_db)):
    all_db_constructors = constructor_service.get_all_constructors(db, offset=offset, page_count=page_count)
    return all_db_constructors
