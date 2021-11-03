from __future__ import annotations
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
from http import HTTPStatus

from fastapi import Depends, HTTPException, Request
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi.security import OAuth2, OAuth2PasswordBearer
from fastapi.security.utils import get_authorization_scheme_param
from jose import JWTError, jwt
from tortoise.exceptions import DoesNotExist

from src.main import OAuth2PasswordBearerCookie
from src.schemas.token import TokenData
from src.schemas.users import UserOutSchema
from src.database.models import Users

load_dotenv()
SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


security = OAuth2PasswordBearerCookie(tokenUrl="/login")
# security = OAuth2PasswordBearer(tokenUrl="/login")


def create_access_token(data: dict, expires_delta: timedelta = None):
    """Generates access token for user

    Args:
        data (dict): [description]
        expires_delta (timedelta, optional): [description]. Defaults to None.

    Returns:
        str: JWT token
    """
    to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


async def get_current_user(token: str = Depends(security)):
    """Decodes token and validate user

    Args:
        token (str, optional): [description]. Defaults to Depends(Security).

    Raises:
        credentials_exception: [description]
        credentials_exception: [description]
        credentials_exception: [description]

    Returns:
        [type]: user Object
    """
    credentials_exception = HTTPException(
        status_code=HTTPStatus.UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    try:
        user = await UserOutSchema.from_queryset_single(
            Users.get(username=token_data.username)
        )
    except DoesNotExist:
        raise credentials_exception
    return user
