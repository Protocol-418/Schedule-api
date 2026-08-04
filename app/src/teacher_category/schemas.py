from typing import Annotated

from pydantic import Field

from app.core.base_schemas import CustomBaseModel

TeacherCategoryName = Annotated[str, Field(min_length=1, max_length=50, description="Название категории преподавателя", examples=["Высшая"])]


class BaseTeacherCategoryModel(CustomBaseModel):
    """Базовая схема со всеми возможными полями (все nullable для гибкости)"""
    name: TeacherCategoryName | None = None


class CreateTeacherCategory(BaseTeacherCategoryModel):
    """Схема создания"""
    name: TeacherCategoryName


class UpdateTeacherCategory(BaseTeacherCategoryModel):
    """Схема обновления"""


class ShowTeacherCategory(BaseTeacherCategoryModel):
    """Схема ответа"""
    id: Annotated[int, Field(description="ID категории", examples=[418])]
    name: TeacherCategoryName
