from typing import Annotated
from pydantic import BaseModel, Field


class CreateTeacherCategory(BaseModel):
    name: Annotated[
        str,
        Field(min_length=1, max_length=50)
    ] = Field(
        ...,
        description="Название категории преподавателя",
        examples=["Высшая"]
    )


class UpdateTeacherCategory(BaseModel):
    name: Annotated[
        str,
        Field(min_length=1, max_length=50)
    ] | None = Field(
        None,
        description="Название категории преподавателя"
    )


class ShowTeacherCategory(BaseModel):
    name: str = Field(..., description="Название категории преподавателя")

    model_config = {
        "from_attributes": True
    }