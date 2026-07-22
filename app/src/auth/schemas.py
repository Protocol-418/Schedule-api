from typing import Annotated
from pydantic import Field, EmailStr
from app.core.base_schemas import CustomBaseModel


class LoginRequest(CustomBaseModel):
    email: Annotated[EmailStr, Field(description="Почта пользователя", examples=["user_example_email@email.com"])]
    password: Annotated[str, Field(min_length=6, max_length=25, description="Пароль пользователя", examples=["password123"])]
     