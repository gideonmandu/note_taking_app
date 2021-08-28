import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.database.register import register_tortoise
from src.database.config import TORTOISE_ORM


def get_application():
    _app = FastAPI(title=os.environ.get("PROJECT_NAME"))

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[os.environ.get("BACKEND_CORS_ORIGINS")],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app


app = get_application()
register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False)

@app.get("/")
def home():
    return "hello, world!"