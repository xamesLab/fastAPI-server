from fastapi import FastAPI

from src.router import api_router

app = FastAPI(
    title="api App",
)


app.include_router(api_router)
