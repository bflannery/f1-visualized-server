from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db import get_db
from schemas import ConstructorSchema, ConstructorResultSchema
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
def get_all_constructors(db: Session = Depends(get_db)):
    all_db_constructors = constructor_service.get_all_constructors(db)
    return all_db_constructors


@constructors_router.get(
    "/{result_id}",
    summary="Get constructor result by id",
    response_model=ConstructorResultSchema
)
def get_constructor_by_id(result_id: int, db: Session = Depends(get_db)):
    db_constructor_result = constructor_service.get_constructor_result_by_id(db, id=result_id)
    if db_constructor_result is None:
        raise HTTPException(status_code=404, detail=f"Constructor Result #{result_id} not found")
    return db_constructor_result


@constructors_router.get(
    "/{constructor_id}",
    summary="Get constructor result by constructor id",
    response_model=list[ConstructorResultSchema]
)
def get_constructor_by_id(constructor_id: int, db: Session = Depends(get_db)):
    db_constructor_results = constructor_service.get_constructor_results_by_constructor_id(db,
                                                                                           constructor_id=constructor_id)
    if db_constructor_results is None:
        raise HTTPException(status_code=404, detail=f"Constructor #{constructor_id} not found")
    return db_constructor_results


@constructors_router.get(
    "",
    summary="Get all constructors results",
    response_model=list[ConstructorResultSchema]
)
def get_all_constructors_results(db: Session = Depends(get_db)):
    all_db_constructors_results = constructor_service.get_all_constructors_results(db)
    return all_db_constructors_results
