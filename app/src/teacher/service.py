from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.base_schemas import Pagination
from app.core.dependies import get_db
from app.core.exceptions.exceptions import NotFoundException
from app.db.models.teacher import Teacher
from app.src.teacher.repository import TeacherRepository
from app.src.teacher.schemas import CreateTeacher, UpdateTeacher
from app.src.teacher_category.service import TeacherCategoryService


class TeacherService:
    def __init__(self, session: Annotated[AsyncSession, Depends(get_db)]):
        self.session = session
        self.teacher_repo = TeacherRepository(self.session)
        self.category_service = TeacherCategoryService(self.session)

    async def _get_teacher_by_id(self, id: int) -> Teacher:
        """Получение преподавателя по id"""
        teacher = await self.teacher_repo.get_entity_by_filter(id=id)
        if not teacher:
            raise NotFoundException(service="Teacher", message="Преподаватель с таким id не найден")
        return teacher

    async def _get_all_teachers(self, pagination: Pagination) -> list[Teacher]:
        """Получение всех преподавателей"""
        teachers = await self.teacher_repo.get_all_entities(pagination=pagination)
        return teachers

    async def _create_teacher(self, teacher_data: CreateTeacher) -> Teacher:
        """Создание нового преподавателя"""
        if teacher_data.teacher_category is not None:
            await self.category_service._get_category_by_name(teacher_data.teacher_category)

        teacher = Teacher(
            name=teacher_data.name,
            surname=teacher_data.surname,
            lastname=teacher_data.lastname,
            phone_number=teacher_data.phone_number,
            email=teacher_data.email,
            teacher_category=teacher_data.teacher_category
        )

        new_teacher = await self.teacher_repo.create_entity(teacher)
        return new_teacher

    async def _delete_teacher(self, id: int) -> bool:
        """Удаление преподавателя"""
        teacher = await self._get_teacher_by_id(id)
        delete_result = await self.teacher_repo.delete_entity(teacher)
        return delete_result

    async def _clear_category(self, id: int) -> Teacher:
        """Очистка категории преподавателя"""
        teacher = await self._get_teacher_by_id(id)
        teacher.teacher_category = None
        return await self.teacher_repo.update_entity(teacher)

    async def _update_teacher(self, id: int, teacher_data: UpdateTeacher) -> Teacher:
        """Обновление преподавателя"""
        teacher = await self._get_teacher_by_id(id)

        if teacher_data.teacher_category is not None:
            await self.category_service._get_category_by_name(teacher_data.teacher_category)

        updated_teacher_data = teacher_data.model_dump(exclude_unset=True)
        for field, value in updated_teacher_data.items():
            setattr(teacher, field, value)

        updated_teacher = await self.teacher_repo.update_entity(teacher)
        return updated_teacher