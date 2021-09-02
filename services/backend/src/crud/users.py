from fastapi import HTTPException
from passlib.context import CryptContext
from tortoise.exceptions import DoesNotExist, IntegrityError

from src.database.models import Users
from src.schemas.token import Status
from src.schemas.users import UserOutSchema


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def create_user(user) -> UserOutSchema:
    """Create a user

    Args:
        user ([type]): [description]

    Raises:
        HTTPException: [description]

    Returns:
        UserOutSchema: user object
    """
    user.password = pwd_context.encrypt(user.password)
    
    try:
        user_obj = await Users.create(**user.dict(exclude_unset=True))
    except IntegrityError:
        raise HTTPException(
            status_code=401, detail=f"Sorry, that username already exists"
        )
    return await UserOutSchema.from_tortoise_orm(user_obj)


async def delete_user(user_id, current_user) -> Status:
    """Remove user from database

    Args:
        user_id ([type]): [description]
        current_user ([type]): [description]

    Raises:
        HTTPException: [description]
        HTTPException: [description]
        HTTPException: [description]

    Returns:
        str: message
    """
    error_msg = f"User {user_id} not found."
    try:
        db_user = await UserOutSchema.from_queryset_single(
            Users.get(id=user_id)
        )
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=error_msg)
    if db_user.id == current_user.id:
        deleted_count = await Users.filter(id=user_id).delete()
        if not deleted_count:
            raise HTTPException(status_code=404, detail=error_msg)
        return Status(message=f"Deleted user {user_id}.")
    raise HTTPException(Status_code=403, detail=f"Not authorized to delete.")
