from typing import Annotated
from pydantic import BaseModel, Field, EmailStr


class CreateTeacher(BaseModel):
    name: Annotated[
        str,
        Field(min_length=1, max_length=100)
    ] = Field(
        ...,
        description="Имя преподавателя",
        examples=["Иван"]
    )
    surname: Annotated[
        str,
        Field(min_length=1, max_length=100)
    ] = Field(
        ...,
        description="Фамилия преподавателя",
        examples=["Иванов"]
    )
    lastname: Annotated[
        str,
        Field(max_length=100)
    ] | None = Field(
        None,
        description="Отчество преподавателя",
        examples=["Иванович"]
    )
    phone_number: Annotated[
        str,
        Field(max_length=20)
    ] | None = Field(
        None,
        description="Номер телефона",
        examples=["+7 999 123-45-67"]
    )
    email: Annotated[
        str,
        Field(max_length=100)
    ] | None = Field(
        None,
        description="Электронная почта",
        examples=["ivanov@example.com"]
    )
    teacher_category: Annotated[
        str,
        Field(max_length=50)
    ] | None = Field(
        None,
        description="Категория преподавателя",
        examples=["Высшая"]
    )


class UpdateTeacher(BaseModel):
    name: Annotated[
        str,
        Field(min_length=1, max_length=100)
    ] | None = Field(
        None,
        description="Имя преподавателя"
    )
    surname: Annotated[
        str,
        Field(min_length=1, max_length=100)
    ] | None = Field(
        None,
        description="Фамилия преподавателя"
    )
    lastname: Annotated[
        str,
        Field(max_length=100)
    ] | None = Field(
        None,
        description="Отчество преподавателя"
    )
    phone_number: Annotated[
        str,
        Field(max_length=20)
    ] | None = Field(
        None,
        description="Номер телефона"
    )
    email: Annotated[
        str,
        Field(max_length=100)
    ] | None = Field(
        None,
        description="Электронная почта"
    )
    teacher_category: Annotated[
        str,
        Field(max_length=50)
    ] | None = Field(
        None,
        description="Категория преподавателя"
    )


class ShowTeacher(BaseModel):
    id: int = Field(..., description="ID преподавателя")
    name: str = Field(..., description="Имя преподавателя")
    surname: str = Field(..., description="Фамилия преподавателя")
    lastname: str | None = Field(None, description="Отчество преподавателя")
    phone_number: str | None = Field(None, description="Номер телефона")
    email: str | None = Field(None, description="Электронная почта")
    teacher_category: str | None = Field(None, description="Категория преподавателя")

    model_config = {
        "from_attributes": True
    }