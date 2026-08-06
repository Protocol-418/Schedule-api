from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.dependies import get_db
from app.core.exceptions.exceptions import ConflictException, NotFoundException
from app.db.models.specialty import Specialty
from app.src.speciality.repository import SpecialtyRepository
from app.src.speciality.schemas import CreateSpecialty, UpdateSpecialty


class SpecialtyService:
    def __init__(self, session: Annotated[AsyncSession, Depends(get_db)]):
        self.session = session
        self.specialty_repo = SpecialtyRepository(self.session)

    async def _get_specialty_by_code(self, code: str) -> Specialty:
        """Получение специальности по коду"""
        specialty = await self.specialty_repo.get_entity_by_filter(code=code)
        if not specialty:
            raise NotFoundException(service="Specialty", message="Специальность с таким кодом не найдена")
        return specialty

    async def _get_all_specialties(self) -> list[Specialty]:
        """Получение всех специальностей"""
        specialties = await self.specialty_repo.get_all_entities()
        return specialties

    async def _create_specialty(self, specialty_data: CreateSpecialty) -> Specialty:
        """Создание новой специальности"""
        is_exist = await self.specialty_repo.get_entity_by_filter(code=specialty_data.code)
        if is_exist:
            raise ConflictException(message="Специальность с таким кодом уже существует", service="Specialty")

        specialty = Specialty(
            code=specialty_data.code,
            title=specialty_data.title,
        )

        new_specialty = await self.specialty_repo.create_entity(specialty)
        return new_specialty

    async def _delete_specialty(self, code: str) -> bool:
        """Удаление специальности"""
        specialty = await self._get_specialty_by_code(code)
        delete_result = await self.specialty_repo.delete_entity(specialty)
        return delete_result

    async def _update_specialty(self, code: str, specialty_data: UpdateSpecialty) -> Specialty:
        """Обновление специальности"""
        specialty = await self._get_specialty_by_code(code)

        updated_data = specialty_data.model_dump(exclude_unset=True)
        for field, value in updated_data.items():
            setattr(specialty, field, value)

        updated_specialty = await self.specialty_repo.update_entity(specialty)
        return updated_specialty
