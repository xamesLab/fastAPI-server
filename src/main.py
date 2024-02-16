from fastapi import FastAPI

from src.auth.base_config import auth_backend, fastapi_users
from src.auth.schemas import UserRead, UserCreate

from src.operations.rouner import router as router_operation

app = FastAPI(title="test App")


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(router_operation)
