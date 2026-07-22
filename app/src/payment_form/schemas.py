from typing import Annotated
from pydantic import Field
from app.core.base_schemas import CustomBaseModel


PaymentFormName = Annotated[str, Field(min_length=1, max_length=50, description="Название формы оплаты", examples=["Бюджетная"])]
IsStateFunded = Annotated[bool, Field(description="Флаг: является ли бюджетной формой обучения", examples=[True])]


class BasePaymentFormModel(CustomBaseModel):
    """Базовая схема со всеми возможными полями (все nullable для гибкости)"""
    name: PaymentFormName | None = None
    is_state_funded: IsStateFunded | None = None


class CreatePaymentForm(BasePaymentFormModel):
    """Схема создания"""
    name: PaymentFormName
    is_state_funded: IsStateFunded


class UpdatePaymentForm(BasePaymentFormModel):
    """Схема обновления"""
    pass


class ShowPaymentForm(BasePaymentFormModel):
    """Схема ответа"""
    name: PaymentFormName
    is_state_funded: IsStateFunded
