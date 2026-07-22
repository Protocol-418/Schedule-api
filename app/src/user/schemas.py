from typing import Annotated
from uuid import UUID
from pydantic import Field, EmailStr, StringConstraints
from app.core.base_schemas import CustomBaseModel


UserEmail = Annotated[EmailStr, Field(max_length=100, description="Электронная почта", examples=["user@example.com"])]
Username = Annotated[str, Field(min_length=3, max_length=30, description="Публичное имя пользователя", examples=["ivan_ivanov"])]
UserPassword = Annotated[str, Field(min_length=8, max_length=128, description="Сложный пароль (минимум 8 символов)", examples=["StrongPassword123!"])]
UserRole = Annotated[str, Field(max_length=50, description="Роль пользователя", examples=["admin"])]


class BaseUserModel(CustomBaseModel):
    """Базовая схема со всеми возможными полями (все nullable для гибкости)"""
    username: Username | None = None
    email: UserEmail | None = None
    role: UserRole | None = None


class CreateUser(BaseUserModel):
    """Схема создания"""
    email: UserEmail
    password: UserPassword
    role: UserRole = "admin"


class UpdateUser(BaseUserModel):
    """Схема обновления"""
    pass


class ShowUser(BaseUserModel):
    """Схема ответа"""
    uuid: Annotated[UUID, Field(description="ID пользователя")]
    username: Username
    email: UserEmail
    role: UserRole
    is_active: Annotated[bool, Field(description="Статус активности аккаунта")]
