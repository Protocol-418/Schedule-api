from typing import Annotated

from pydantic import Field

from app.core.base_schemas import CustomBaseModel

ClassSessionTypeName = Annotated[
    str,
    Field(
        min_length=1,
        max_length=50,
        description="Название типа занятия",
        examples=["ЛК"],
    ),
]

IsStream = Annotated[
    bool,
    Field(
        description="Флаг, обозначающий, является ли тип пары потоковым",
        examples=[True],
    ),
]


class BaseClassSessionTypeModel(CustomBaseModel):
    """Базовая схема со всеми возможными полями (все nullable для гибкости)"""

    name: ClassSessionTypeName | None = None
    is_stream: IsStream | None = None


class CreateClassSessionType(BaseClassSessionTypeModel):
    """Схема создания"""

    name: ClassSessionTypeName
    is_stream: IsStream


class UpdateClassSessionType(BaseClassSessionTypeModel):
    """Схема обновления"""


class ShowClassSessionType(BaseClassSessionTypeModel):
    """Схема ответа"""

    name: ClassSessionTypeName
    is_stream: IsStream
