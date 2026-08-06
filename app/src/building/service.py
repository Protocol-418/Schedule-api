from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.dependies import get_db
from app.core.exceptions.exceptions import ConflictException, NotFoundException
from app.db.models.building import Building
from app.src.building.repository import BuildingRepository
from app.src.building.schemas import CreateBuilding, UpdateBuilding


class BuildingService:
    def __init__(self, session: Annotated[AsyncSession, Depends(get_db)]):
        self.session = session
        self.building_repo = BuildingRepository(self.session)

    async def _get_building_by_number(self, number: int) -> Building:
        """Получение корпуса по номеру"""
        building = await self.building_repo.get_entity_by_filter(number=number)
        if not building:
            raise NotFoundException(service="Building", message="Корпус с таким номером не найден")
        return building

    async def _get_all_buildings(self) -> list[Building]:
        """Получение всех корпусов"""
        buildings = await self.building_repo.get_all_entities()
        return buildings

    async def _create_building(self, building_data: CreateBuilding) -> Building:
        """Создание нового корпуса"""
        is_exist = await self.building_repo.get_entity_by_filter(number=building_data.number)
        if is_exist:
            raise ConflictException(message="Корпус с таким номером уже существует", service="Building")

        building = Building(
            number=building_data.number,
            city=building_data.city,
            address=building_data.address,
            is_active=building_data.is_active if building_data.is_active is not None else True,
        )

        new_building = await self.building_repo.create_entity(building)
        return new_building

    async def _delete_building(self, number: int) -> bool:
        """Удаление корпуса"""
        building = await self._get_building_by_number(number)
        delete_result = await self.building_repo.delete_entity(building)
        return delete_result

    async def _update_building(self, number: int, building_data: UpdateBuilding) -> Building:
        """Обновление корпуса"""
        building = await self._get_building_by_number(number)

        updated_data = building_data.model_dump(exclude_unset=True)
        for field, value in updated_data.items():
            setattr(building, field, value)

        updated_building = await self.building_repo.update_entity(building)
        return updated_building
