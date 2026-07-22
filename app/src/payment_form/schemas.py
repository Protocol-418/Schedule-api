from typing import Annotated
from pydantic import BaseModel, Field


class CreatePaymentForm(BaseModel):
    name: Annotated[
        str,
        Field(min_length=1, max_length=50)
    ] = Field(
        ...,
        description="Название формы оплаты",
        examples=["Бюджетная"]
    )
    is_state_funded: Annotated[
        bool,
        Field()
    ] = Field(
        ...,
        description="Является ли бюджетной формой обучения",
        examples=[True]
    )


class UpdatePaymentForm(BaseModel):
    name: Annotated[
        str,
        Field(min_length=1, max_length=50)
    ] | None = Field(
        None,
        description="Название формы оплаты"
    )
    is_state_funded: Annotated[
        bool,
        Field()
    ] | None = Field(
        None,
        description="Является ли бюджетной формой обучения"
    )


class ShowPaymentForm(BaseModel):
    name: str = Field(..., description="Название формы оплаты")
    is_state_funded: bool = Field(..., description="Является ли бюджетной формой обучения")

    model_config = {
        "from_attributes": True
    }
