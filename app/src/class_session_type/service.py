from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.dependies import get_db
from app.core.exceptions.exceptions import ConflictException, NotFoundException
from app.db.models.class_session_type import ClassSessionType
from app.src.class_session_type.repository import ClassSessionTypeRepository
from app.src.class_session_type.schemas import (
    CreateClassSessionType,
    UpdateClassSessionType,
)


class ClassSessionTypeService:
    def __init__(self, session: Annotated[AsyncSession, Depends(get_db)]):
        self.session = session
        self.type_repo = ClassSessionTypeRepository(self.session)

    async def _get_type_by_name(self, name: str) -> ClassSessionType:
        """Получение типа занятия по названию"""
        session_type = await self.type_repo.get_entity_by_filter(name=name)
        if not session_type:
            raise NotFoundException(service="ClassSessionType", message="Тип занятия с таким названием не найден")
        return session_type

    async def _get_all_types(self) -> list[ClassSessionType]:
        """Получение всех типов занятий"""
        types = await self.type_repo.get_all_entities()
        return types

    async def _create_type(self, type_data: CreateClassSessionType) -> ClassSessionType:
        """Создание нового типа занятия"""
        is_exist = await self.type_repo.get_entity_by_filter(name=type_data.name)
        if is_exist:
            raise ConflictException(
                message="Тип занятия с таким названием уже существует",
                service="ClassSessionType",
            )

        new_type = ClassSessionType(name=type_data.name)
        created_type = await self.type_repo.create_entity(new_type)
        return created_type

    async def _delete_type(self, name: str) -> bool:
        """Удаление типа занятия"""
        session_type = await self._get_type_by_name(name)
        delete_result = await self.type_repo.delete_entity(session_type)
        return delete_result

    async def _update_type(self, name: str, type_data: UpdateClassSessionType) -> ClassSessionType:
        """Обновление типа занятия"""
        session_type = await self._get_type_by_name(name)

        updated_data = type_data.model_dump(exclude_unset=True)
        for field, value in updated_data.items():
            setattr(session_type, field, value)

        updated_type = await self.type_repo.update_entity(session_type)
        return updated_type
