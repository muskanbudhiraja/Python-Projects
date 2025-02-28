from fastapi import APIRouter
from src.api.v1.routes.health import healthCheck

router = APIRouter()
router.include_router(healthCheck,prefix="/v1")