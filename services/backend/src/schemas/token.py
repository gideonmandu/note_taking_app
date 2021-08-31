from pydantic import BaseModel
from typing import Optional


class TokenData(BaseModel):
    username: Optional[str]


class Status(BaseModel):
    message: str