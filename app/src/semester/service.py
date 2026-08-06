from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.dependies import get_db
from app.core.exceptions.exceptions import NotFoundException
from app.db.models.semester import Semester
from app.src.plan.service import PlanService
from app.src.semester.repository import SemesterRepository
from app.src.semester.schemas import CreateSemester, UpdateSemester


class SemesterService:
    def __init__(self, session: Annotated[AsyncSession, Depends(get_db)]):
        self.session = session
        self.semester_repo = SemesterRepository(self.session)
        self.plan_service = PlanService(self.session)

    async def _get_semester_by_id(self, semester_id: int) -> Semester:
        """Получение семестра по ID"""
        semester = await self.semester_repo.get_entity_by_filter(id=semester_id)
        if not semester:
            raise NotFoundException(service="Semester", message="Семестр с таким ID не найден")
        return semester

    async def _get_all_semesters(self) -> list[Semester]:
        """Получение всех семестров"""
        semesters = await self.semester_repo.get_all_entities()
        return semesters

    async def _get_semesters_by_plan(self, plan_id: int) -> list[Semester]:
        """Получение всех семестров конкретного учебного плана"""
        await self.plan_service._get_plan_by_id(plan_id)
        semesters = await self.semester_repo.get_entities_by_filter(plan_id=plan_id)
        return semesters

    async def _create_semester(self, semester_data: CreateSemester) -> Semester:
        """Создание нового семестра"""
        await self.plan_service._get_plan_by_id(semester_data.plan_id)

        semester = Semester(
            semester_number=semester_data.semester_number,
            weeks=semester_data.weeks,
            practice_weeks=semester_data.practice_weeks,
            plan_id=semester_data.plan_id,
        )

        new_semester = await self.semester_repo.create_entity(semester)
        return new_semester

    async def _delete_semester(self, semester_id: int) -> bool:
        """Удаление семестра"""
        semester = await self._get_semester_by_id(semester_id)
        delete_result = await self.semester_repo.delete_entity(semester)
        return delete_result

    async def _update_semester(self, semester_id: int, semester_data: UpdateSemester) -> Semester:
        """Обновление семестра"""
        semester = await self._get_semester_by_id(semester_id)

        updated_data = semester_data.model_dump(exclude_unset=True)
        if "plan_id" in updated_data:
            await self.plan_service._get_plan_by_id(updated_data["plan_id"])

        for field, value in updated_data.items():
            setattr(semester, field, value)

        updated_semester = await self.semester_repo.update_entity(semester)
        return updated_semester
