from app.core.dependies import get_db
from app.core.exceptions.exceptions import NotFoundException, ConflictException
from app.src.teacher_category.repository import TeacherCategoryRepository
from app.src.teacher_category.schemas import CreateTeacherCategory, UpdateTeacherCategory
from app.db.models.teachers_category import TeachersCategory

from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession


class TeacherCategoryService:
    def __init__(self, session: Annotated[AsyncSession, Depends(get_db)]):
        self.session = session
        self.category_repo = TeacherCategoryRepository(self.session)

    async def _get_category_by_name(self, name: str) -> TeachersCategory:
        """Получение категории по названию"""
        category = await self.category_repo.get_entity_by_filter(name=name)
        if not category:
            raise NotFoundException(service="TeacherCategory", message="Категория с таким названием не найдена")
        return category

    async def _get_all_categories(self) -> list[TeachersCategory]:
        """Получение всех категорий"""
        categories = await self.category_repo.get_all_entities()
        return categories

    async def _create_category(self, category_data: CreateTeacherCategory) -> TeachersCategory:
        """Создание новой категории"""
        is_exist = await self.category_repo.get_entity_by_filter(name=category_data.name)
        if is_exist:
            raise ConflictException(message="Категория с таким названием уже существует", service="TeacherCategory")

        category = TeachersCategory(name=category_data.name)
        new_category = await self.category_repo.create_entity(category)
        return new_category

    async def _delete_category(self, name: str) -> bool:
        """Удаление категории"""
        category = await self._get_category_by_name(name)
        delete_result = await self.category_repo.delete_entity(category)
        return delete_result

    async def _update_category(self, name: str, category_data: UpdateTeacherCategory) -> TeachersCategory:
        """Обновление категории"""
        category = await self._get_category_by_name(name)

        updated_data = category_data.model_dump(exclude_unset=True)
        for field, value in updated_data.items():
            setattr(category, field, value)

        updated_category = await self.category_repo.update_entity(category)
        return updated_category