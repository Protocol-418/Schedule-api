from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel


class CustomBaseModel(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,  # Позволяет принимать поля не только по названию, но и по алиасу
        alias_generator=to_camel,  # Автоматически создаёт алиасы для python полей по правилам camel_case
    )


class Pagination(CustomBaseModel):
    page: Annotated[
        int,
        Field(
            default=0,
            description="Страница данных, с которой будем их брать",
            examples=[0],
        ),
    ]
    limit: Annotated[
        int,
        Field(
            default=100,
            description="Количество записей на одной странице данных",
            examples=[100],
        ),
    ]
