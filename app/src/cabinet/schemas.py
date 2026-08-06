from typing import Annotated

from pydantic import Field

from app.core.base_schemas import CustomBaseModel

CabinetNumber = Annotated[int, Field(gt=0, description="Номер кабинета", examples=[101])]
CabinetCapacity = Annotated[int, Field(ge=0, description="Вместимость кабинета", examples=[30])]
CabinetState = Annotated[str, Field(max_length=50, description="Состояние кабинета", examples=["Хорошее"])]
BuildingNumber = Annotated[int, Field(gt=0, description="Номер корпуса", examples=[1])]


class BaseCabinetModel(CustomBaseModel):
    """Базовая схема со всеми возможными полями (все nullable для гибкости)"""
    number: CabinetNumber | None = None
    capacity: CabinetCapacity | None = None
    state: CabinetState | None = None
    building_number: BuildingNumber | None = None


class CreateCabinet(BaseCabinetModel):
    """Схема создания"""
    number: CabinetNumber
    capacity: CabinetCapacity
    building_number: BuildingNumber


class UpdateCabinet(BaseCabinetModel):
    """Схема обновления"""


class ShowCabinet(BaseCabinetModel):
    """Схема ответа"""
    id: Annotated[int, Field(description="ID кабинета", examples=[418])]
    number: CabinetNumber
    capacity: CabinetCapacity
    building_number: BuildingNumber
