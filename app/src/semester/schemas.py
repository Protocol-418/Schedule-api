from typing import Annotated

from pydantic import Field

from app.core.base_schemas import CustomBaseModel

SemesterNumber = Annotated[int, Field(ge=1, le=12, description="Номер семестра", examples=[1])]
SemesterWeeks = Annotated[float, Field(ge=0, description="Количество недель", examples=[18.0])]
PracticeWeeks = Annotated[float, Field(ge=0, description="Количество недель практики", examples=[4.0])]
PlanId = Annotated[int, Field(gt=0, description="ID учебного плана", examples=[1])]


class BaseSemesterModel(CustomBaseModel):
    """Базовая схема со всеми возможными полями (все nullable для гибкости)"""
    semester_number: SemesterNumber | None = None
    weeks: SemesterWeeks | None = None
    practice_weeks: PracticeWeeks | None = None
    plan_id: PlanId | None = None


class CreateSemester(BaseSemesterModel):
    """Схема создания"""
    semester_number: SemesterNumber
    weeks: SemesterWeeks
    practice_weeks: PracticeWeeks
    plan_id: PlanId


class UpdateSemester(BaseSemesterModel):
    """Схема обновления"""


class ShowSemester(BaseSemesterModel):
    """Схема ответа"""
    id: Annotated[int, Field(description="ID семестра", examples=[1])]
    semester_number: SemesterNumber
    weeks: SemesterWeeks
    practice_weeks: PracticeWeeks
    plan_id: PlanId
