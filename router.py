from fastapi import APIRouter
from controllers import constructors_router, drivers_router, circuits_router, races_router, seasons_router

api_router = APIRouter()

api_router.include_router(circuits_router, prefix="/circuits", tags=["Circuits"])
api_router.include_router(constructors_router, prefix="/constructors", tags=["Constructors"])
api_router.include_router(drivers_router, prefix="/drivers", tags=["Drivers"])
api_router.include_router(races_router, prefix="/races", tags=["Races"])
api_router.include_router(seasons_router, prefix="/seasons", tags=["Seasons"])
