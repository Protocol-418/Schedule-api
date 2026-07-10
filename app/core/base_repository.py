from app.db.models.base import Base

from typing import TypeVar

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select

# Тип модели для аннотации функций
ModelType = TypeVar("ModelType", bound=Base) 

class BaseRepository:
    """Базовый класс слоя репозиториев, нужен для базовых crud-операций"""
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_entities(self) -> list[ModelType]:
        """Метод получения всех записей"""
        stmt = select(self.model)
        result = await self.session.execute(stmt)
        return list(result.scalars().all())

    async def get_entity_by_filter(self, **kwargs) -> ModelType | None:
        """Метод для получения одной записи по заданному фильтру"""
        stmt = select(self.model).filter_by(**kwargs)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def get_entities_by_filter(self, **kwargs) -> list[ModelType]:
        """Метод для получения множества записей по заданному фильтру"""
        stmt = select(self.model).filter_by(**kwargs)
        result = await self.session.execute(stmt)
        return list(result.scalars().all()) or []

    async def create_entity(self, entity: ModelType) -> ModelType:
        """Метод для создания записи"""
        self.session.add(entity)
        await self.session.commit()
        await self.session.refresh(entity) # Актуализируем данные о записи
        return entity

    async def delete_entity(self, entity: ModelType) -> bool:
        """Метод для удаления записи"""
        try:
            await self.session.delete(entity)
            await self.session.commit()
            return True
        except SQLAlchemyError as e:
            self.session.rollback()  # Откатываем сессию при ошибке
            raise e

    async def update_entity(self, entity: ModelType) -> ModelType:
        """Метод для обновления данных"""
        try:
            await self.session.commit()
            await self.session.refresh(entity)
            return entity
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e
    