from typing import Annotated

from pydantic import Field

from app.core.base_schemas import CustomBaseModel

BuildingNumber = Annotated[int, Field(gt=0, description="Номер корпуса", examples=[1])]
BuildingCity = Annotated[str, Field(max_length=100, description="Город корпуса", examples=["Москва"])]
BuildingAddress = Annotated[str, Field(max_length=255, description="Адрес корпуса", examples=["ул. Ленина, 1"])]
IsActive = Annotated[bool, Field(description="Флаг активности корпуса", examples=[True])]


class BaseBuildingModel(CustomBaseModel):
    """Базовая схема со всеми возможными полями (все nullable для гибкости)"""
    number: BuildingNumber | None = None
    city: BuildingCity | None = None
    address: BuildingAddress | None = None
    is_active: IsActive | None = None


class CreateBuilding(BaseBuildingModel):
    """Схема создания"""
    number: BuildingNumber
    city: BuildingCity
    address: BuildingAddress


class UpdateBuilding(BaseBuildingModel):
    """Схема обновления"""


class ShowBuilding(BaseBuildingModel):
    """Схема ответа"""
    number: BuildingNumber
    city: BuildingCity
    address: BuildingAddress
    is_active: IsActive
