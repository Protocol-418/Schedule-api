from uuid import UUID
from typing import Annotated
from pydantic import BaseModel, Field, EmailStr, StringConstraints


class GetUserByEmail(BaseModel):
    email: EmailStr = Field(
        ..., 
        description="Электронная почта пользователя",
        examples=["user@example.com"]
    )


class CreateUser(GetUserByEmail):
    username: Annotated[
        str, 
        StringConstraints(min_length=3, max_length=30)
    ] | None = Field(
        None, 
        description="Публичное имя пользователя",
        examples=["ivan_ivanov"]
    )
    password: Annotated[
        str, 
        StringConstraints(min_length=8, max_length=128)
    ] = Field(
        ..., 
        description="Сложный пароль (минимум 8 символов)",
        examples=["StrongPassword123!"]
    )
    role: str | None = Field(
        "admin", 
        description="Роль при регистрации (по умолчанию 'admin')"
    )


class UpdateUser(BaseModel):
    username: Annotated[
        str,
        StringConstraints(min_length=3, max_length=30)
    ] | None = Field(
        None, 
        description="Публичное имя пользователя",
        examples=["ivan_ivanov"]
    )


class ShowUser(BaseModel):
    uuid: UUID = Field(..., description="ID пользователя")
    username: str | None = Field(None, description="Имя профиля")
    email: EmailStr = Field(..., description="Почта")
    role: str = Field(..., description="Текущая роль")
    is_active: bool = Field(..., description="Статус активности аккаунта")

    model_config = {
        "from_attributes": True  # Позволяет работать с объектами SQLAlchemy
    } 