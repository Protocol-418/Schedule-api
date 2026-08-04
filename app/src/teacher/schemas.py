from typing import Annotated

from pydantic import EmailStr, Field

from app.core.base_schemas import CustomBaseModel

TeacherName = Annotated[str, Field(min_length=1, max_length=100, description="Имя преподавателя", examples=["Иван"])]
TeacherSurname = Annotated[str, Field(min_length=1, max_length=100, description="Фамилия преподавателя", examples=["Иванов"])]
TeacherLastname = Annotated[str, Field(max_length=100, description="Отчество преподавателя", examples=["Иванович"])]
TeacherPhone = Annotated[str, Field(max_length=20, description="Номер телефона", examples=["+7 999 123-45-67"])]
TeacherEmail = Annotated[EmailStr, Field(max_length=100, description="Электронная почта", examples=["ivanov@example.com"])]
TeacherCategory = Annotated[str, Field(max_length=50, description="Категория преподавателя", examples=["Высшая"])]


class BaseTeacherModel(CustomBaseModel):
    """Базовая схема со всеми возможными полями (все nullable для гибкости)"""
    name: TeacherName | None = None
    surname: TeacherSurname | None = None
    lastname: TeacherLastname | None = None
    phone_number: TeacherPhone | None = None
    email: TeacherEmail | None = None
    teacher_category: TeacherCategory | None = None


class CreateTeacher(BaseTeacherModel):
    """Схема создания (в ней переопределяем только то, что строго обязательно)"""
    name: TeacherName
    surname: TeacherSurname


class UpdateTeacher(BaseTeacherModel):
    """Схема обновления"""


class ShowTeacher(BaseTeacherModel):
    """Схема ответа"""
    id: Annotated[int, Field(description="ID преподавателя", examples=[418])]
    name: TeacherName
    surname: TeacherSurname

