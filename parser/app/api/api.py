from fastapi import APIRouter

from app.api.endpoints import channels

api_router = APIRouter()
# api_router.include_router(login.router, tags=["login"])
api_router.include_router(channels.router, prefix="/channels", tags=["channels"])
# api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
# api_router.include_router(items.router, prefix="/items", tags=["items"])
