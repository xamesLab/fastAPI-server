from fastapi import APIRouter

from src.operations.router import operation_router
from src.auth.router import auth_router

api_router = APIRouter(
    prefix="/api/v1",
)


api_router.include_router(operation_router)
api_router.include_router(auth_router)
