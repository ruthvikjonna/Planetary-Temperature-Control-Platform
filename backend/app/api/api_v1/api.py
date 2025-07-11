from fastapi import APIRouter

from app.api.api_v1.endpoints import interventions, satellite_data, intervention_impacts, optimization_results, data_sources, climate_data, ml_optimization

api_router = APIRouter()

# Include all endpoint routers
api_router.include_router(
    interventions.router,
    prefix="/interventions",
    tags=["interventions"]
)

api_router.include_router(
    satellite_data.router,
    prefix="/satellite-data",
    tags=["satellite-data"]
)

api_router.include_router(
    intervention_impacts.router,
    prefix="/intervention-impacts",
    tags=["intervention-impacts"]
)

api_router.include_router(
    optimization_results.router,
    prefix="/optimization-results",
    tags=["optimization-results"]
)

api_router.include_router(
    data_sources.router,
    prefix="/data-sources",
    tags=["data-sources"]
)

api_router.include_router(
    climate_data.router,
    prefix="/climate-data",
    tags=["climate-data"]
)

api_router.include_router(
    ml_optimization.router,
    prefix="/ml-optimization",
    tags=["ml-optimization"]
) 