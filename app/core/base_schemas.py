from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class CustomBaseModel(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True, # Позволяет принимать поля не только по названию, но и по алиасу
        alias_generator=to_camel # Автоматически создаёт алиасы для python полей по правилам camel_case
    )
