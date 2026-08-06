from typing import Annotated

from pydantic import Field

from app.core.base_schemas import CustomBaseModel

GroupName = Annotated[str, Field(min_length=1, max_length=50, description="Название группы", examples=["ИС-21"])]
GroupYearAdmission = Annotated[int, Field(ge=2000, le=2100, description="Год поступления", examples=[2021])]
GroupCountStudents = Annotated[int, Field(ge=0, description="Количество студентов", examples=[25])]
GroupAdvisorId = Annotated[int, Field(gt=0, description="ID куратора (преподавателя)", examples=[1])]
GroupSpecialtyCode = Annotated[str, Field(min_length=1, max_length=20, description="Код специальности", examples=["09.02.07"])]
GroupPaymentForm = Annotated[str, Field(min_length=1, max_length=50, description="Название формы оплаты", examples=["Бюджетная"])]


class BaseGroupModel(CustomBaseModel):
    """Базовая схема со всеми возможными полями (все nullable для гибкости)"""
    name: GroupName | None = None
    year_admission: GroupYearAdmission | None = None
    count_students: GroupCountStudents | None = None
    group_advisor_id: GroupAdvisorId | None = None
    specialty_code: GroupSpecialtyCode | None = None
    payment_form: GroupPaymentForm | None = None


class CreateGroup(BaseGroupModel):
    """Схема создания"""
    name: GroupName
    year_admission: GroupYearAdmission
    count_students: GroupCountStudents
    specialty_code: GroupSpecialtyCode
    payment_form: GroupPaymentForm


class UpdateGroup(BaseGroupModel):
    """Схема обновления"""


class ShowGroup(BaseGroupModel):
    """Схема ответа"""
    name: GroupName
    year_admission: GroupYearAdmission
    count_students: GroupCountStudents
    specialty_code: GroupSpecialtyCode
    payment_form: GroupPaymentForm
