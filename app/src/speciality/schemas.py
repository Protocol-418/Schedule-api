from typing import Annotated

from pydantic import Field

from app.core.base_schemas import CustomBaseModel

SpecialtyCode = Annotated[str, Field(min_length=1, max_length=20, description="Код специальности", examples=["09.02.07"])]
SpecialtyTitle = Annotated[str, Field(max_length=255, description="Название специальности", examples=["Информационные системы и программирование"])]


class BaseSpecialtyModel(CustomBaseModel):
    """Базовая схема со всеми возможными полями (все nullable для гибкости)"""
    code: SpecialtyCode | None = None
    title: SpecialtyTitle | None = None


class CreateSpecialty(BaseSpecialtyModel):
    """Схема создания"""
    code: SpecialtyCode
    title: SpecialtyTitle


class UpdateSpecialty(BaseSpecialtyModel):
    """Схема обновления"""


class ShowSpecialty(BaseSpecialtyModel):
    """Схема ответа"""
    code: SpecialtyCode
    title: SpecialtyTitle
