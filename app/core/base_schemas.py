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
            default=1,
            ge=1,
            description="Страница данных, с которой будем их брать (По умолчанию с первой)",
            examples=[1],
        ),
    ]
    limit: Annotated[
        int,
        Field(
            default=100,
            ge=1,
            le=1000,
            description="Количество записей на одной странице данных (По умолчанию 100 зписей)",
            examples=[100],
        ),
    ]

    @property
    def offset(self) -> int:
        return (self.page - 1) * self.limit
