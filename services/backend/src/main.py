import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise import Tortoise

from src.database.register import register_tortoise
from src.database.config import TORTOISE_ORM

# Enable schema to read r/ship btw models
Tortoise.init_models(["src.database.models"], "models")
from src.routes import users, notes
from src.base import OAuth2PasswordBearerCookie

load_dotenv()


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


def configure_routes(app):
    app.include_router(users.router)
    app.include_router(notes.router)


app = get_application()
configure_routes(app)
register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False)

@app.get("/", include_in_schema=False)
def home():
    return {"message": "hello, world!"}