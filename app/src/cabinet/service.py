from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.dependies import get_db
from app.core.exceptions.exceptions import NotFoundException
from app.db.models.cabinet import Cabinet
from app.src.cabinet.repository import CabinetRepository
from app.src.cabinet.schemas import CreateCabinet, UpdateCabinet


class CabinetService:
    def __init__(self, session: Annotated[AsyncSession, Depends(get_db)]):
        self.session = session
        self.cabinet_repo = CabinetRepository(self.session)

    async def _get_cabinet_by_id(self, cabinet_id: int) -> Cabinet:
        """Получение кабинета по ID"""
        cabinet = await self.cabinet_repo.get_entity_by_filter(id=cabinet_id)
        if not cabinet:
            raise NotFoundException(service="Cabinet", message="Кабинет с таким ID не найден")
        return cabinet

    async def _get_all_cabinets(self) -> list[Cabinet]:
        """Получение всех кабинетов"""
        cabinets = await self.cabinet_repo.get_all_entities()
        return cabinets

    async def _get_cabinets_by_building(self, building_number: int) -> list[Cabinet]:
        """Получение всех кабинетов в конкретном здании"""
        cabinets = await self.cabinet_repo.get_entities_by_filter(building_number=building_number)
        return cabinets

    async def _create_cabinet(self, cabinet_data: CreateCabinet) -> Cabinet:
        """Создание нового кабинета"""
        cabinet = Cabinet(
            number=cabinet_data.number,
            capacity=cabinet_data.capacity,
            state=cabinet_data.state,
            building_number=cabinet_data.building_number,
        )

        new_cabinet = await self.cabinet_repo.create_entity(cabinet)
        return new_cabinet

    async def _delete_cabinet(self, cabinet_id: int) -> bool:
        """Удаление кабинета"""
        cabinet = await self._get_cabinet_by_id(cabinet_id)
        delete_result = await self.cabinet_repo.delete_entity(cabinet)
        return delete_result

    async def _update_cabinet(self, cabinet_id: int, cabinet_data: UpdateCabinet) -> Cabinet:
        """Обновление кабинета"""
        cabinet = await self._get_cabinet_by_id(cabinet_id)

        updated_data = cabinet_data.model_dump(exclude_unset=True)
        for field, value in updated_data.items():
            setattr(cabinet, field, value)

        updated_cabinet = await self.cabinet_repo.update_entity(cabinet)
        return updated_cabinet
