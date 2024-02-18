from fastapi import APIRouter

from src.auth.schemas import UserRead, UserCreate
from src.auth.base_config import fastapi_users, auth_backend

auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

auth_router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/jwt",
)

auth_router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/jwt",
)
