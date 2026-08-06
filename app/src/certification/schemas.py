from typing import Annotated

from pydantic import Field

from app.core.base_schemas import CustomBaseModel

SubjectId = Annotated[int, Field(gt=0, description="ID дисциплины", examples=[1])]


class BaseCertificationModel(CustomBaseModel):
    """Базовая схема со всеми возможными полями (все nullable для гибкости)"""
    subject_id: SubjectId | None = None
    credit: bool | None = None
    differentiated_credit: bool | None = None
    course_project: bool | None = None
    course_work: bool | None = None
    control_work: bool | None = None
    other_form: bool | None = None


class CreateCertification(BaseCertificationModel):
    """Схема создания"""
    subject_id: SubjectId
    credit: bool
    differentiated_credit: bool
    course_project: bool
    course_work: bool
    control_work: bool
    other_form: bool


class UpdateCertification(BaseCertificationModel):
    """Схема обновления"""


class ShowCertification(BaseCertificationModel):
    """Схема ответа"""
    subject_id: SubjectId
    credit: bool
    differentiated_credit: bool
    course_project: bool
    course_work: bool
    control_work: bool
    other_form: bool
