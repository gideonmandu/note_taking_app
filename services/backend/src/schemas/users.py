from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Users


# creating new users
UserInSchema = pydantic_model_creator(
    Users, name="UserIn", exclude_readonly=True
)

# retrieving users to be used outside in app
UserOutSchema = pydantic_model_creator(
    Users, name="UserOut", exclude=["password", "created_at", "modified_at"]
)


# retrieved users to be used in app
UserDatabaseSchema = pydantic_model_creator(
    Users, name="User", exclude=["created_at", "modified_at"]
)