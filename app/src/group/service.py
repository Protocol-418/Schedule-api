from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.base_schemas import Pagination
from app.core.dependies import get_db
from app.core.exceptions.exceptions import ConflictException, NotFoundException
from app.db.models.group import Group
from app.src.group.repository import GroupRepository
from app.src.group.schemas import CreateGroup, UpdateGroup
from app.src.payment_form.service import PaymentFormService
from app.src.speciality.service import SpecialtyService
from app.src.teacher.service import TeacherService


class GroupService:
    def __init__(self, session: Annotated[AsyncSession, Depends(get_db)]):
        self.session = session
        self.group_repo = GroupRepository(self.session)
        self.specialty_service = SpecialtyService(self.session)
        self.payment_form_service = PaymentFormService(self.session)
        self.teacher_service = TeacherService(self.session)

    async def _get_group_by_name(self, name: str) -> Group:
        """Получение группы по названию"""
        group = await self.group_repo.get_entity_by_filter(name=name)
        if not group:
            raise NotFoundException(service="Group", message="Группа с таким названием не найдена")
        return group

    async def _get_all_groups(self, pagination: Pagination) -> list[Group]:
        """Получение всех групп"""
        groups = await self.group_repo.get_all_entities(pagination=pagination)
        return groups

    async def _get_groups_by_specialty(self, specialty_code: str, pagination: Pagination) -> list[Group]:
        """Получение всех групп по коду специальности"""
        await self.specialty_service._get_specialty_by_code(specialty_code)
        groups = await self.group_repo.get_entities_by_filter(
            pagination=pagination, specialty_code=specialty_code
        )
        return groups

    async def _create_group(self, group_data: CreateGroup) -> Group:
        """Создание новой группы"""
        is_exist = await self.group_repo.get_entity_by_filter(name=group_data.name)
        if is_exist:
            raise ConflictException(message="Группа с таким названием уже существует", service="Group")

        await self.specialty_service._get_specialty_by_code(group_data.specialty_code)
        await self.payment_form_service._get_payment_form_by_name(group_data.payment_form)
        if group_data.group_advisor_id is not None:
            await self.teacher_service._get_teacher_by_id(group_data.group_advisor_id)

        group = Group(
            name=group_data.name,
            year_admission=group_data.year_admission,
            count_students=group_data.count_students,
            group_advisor_id=group_data.group_advisor_id,
            specialty_code=group_data.specialty_code,
            payment_form=group_data.payment_form,
        )

        new_group = await self.group_repo.create_entity(group)
        return new_group

    async def _delete_group(self, name: str) -> bool:
        """Удаление группы"""
        group = await self._get_group_by_name(name)
        delete_result = await self.group_repo.delete_entity(group)
        return delete_result

    async def _update_group(self, name: str, group_data: UpdateGroup) -> Group:
        """Обновление группы"""
        group = await self._get_group_by_name(name)

        updated_data = group_data.model_dump(exclude_unset=True)
        if "specialty_code" in updated_data:
            await self.specialty_service._get_specialty_by_code(updated_data["specialty_code"])
        if "payment_form" in updated_data:
            await self.payment_form_service._get_payment_form_by_name(updated_data["payment_form"])
        if "group_advisor_id" in updated_data and updated_data["group_advisor_id"] is not None:
            await self.teacher_service._get_teacher_by_id(updated_data["group_advisor_id"])

        for field, value in updated_data.items():
            setattr(group, field, value)

        updated_group = await self.group_repo.update_entity(group)
        return updated_group
