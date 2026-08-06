from typing import Annotated

from pydantic import Field

from app.core.base_schemas import CustomBaseModel

PlanYear = Annotated[int, Field(ge=2000, le=2100, description="Год учебного плана", examples=[2024])]
PlanSpecialtyCode = Annotated[str, Field(min_length=1, max_length=20, description="Код специальности", examples=["09.02.07"])]


class BasePlanModel(CustomBaseModel):
    """Базовая схема со всеми возможными полями (все nullable для гибкости)"""
    year: PlanYear | None = None
    specialty_code: PlanSpecialtyCode | None = None


class CreatePlan(BasePlanModel):
    """Схема создания"""
    year: PlanYear
    specialty_code: PlanSpecialtyCode


class UpdatePlan(BasePlanModel):
    """Схема обновления"""


class ShowPlan(BasePlanModel):
    """Схема ответа"""
    id: Annotated[int, Field(description="ID учебного плана", examples=[1])]
    year: PlanYear
    specialty_code: PlanSpecialtyCode
