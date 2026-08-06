from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.dependies import get_db
from app.core.exceptions.exceptions import NotFoundException
from app.db.models.plan import Plan
from app.src.plan.repository import PlanRepository
from app.src.plan.schemas import CreatePlan, UpdatePlan
from app.src.speciality.service import SpecialtyService


class PlanService:
    def __init__(self, session: Annotated[AsyncSession, Depends(get_db)]):
        self.session = session
        self.plan_repo = PlanRepository(self.session)
        self.specialty_service = SpecialtyService(self.session)

    async def _get_plan_by_id(self, plan_id: int) -> Plan:
        """Получение учебного плана по ID"""
        plan = await self.plan_repo.get_entity_by_filter(id=plan_id)
        if not plan:
            raise NotFoundException(service="Plan", message="Учебный план с таким ID не найден")
        return plan

    async def _get_all_plans(self) -> list[Plan]:
        """Получение всех учебных планов"""
        plans = await self.plan_repo.get_all_entities()
        return plans

    async def _get_plans_by_specialty(self, specialty_code: str) -> list[Plan]:
        """Получение всех учебных планов по коду специальности"""
        await self.specialty_service._get_specialty_by_code(specialty_code)
        plans = await self.plan_repo.get_entities_by_filter(specialty_code=specialty_code)
        return plans

    async def _create_plan(self, plan_data: CreatePlan) -> Plan:
        """Создание нового учебного плана"""
        await self.specialty_service._get_specialty_by_code(plan_data.specialty_code)

        plan = Plan(
            year=plan_data.year,
            specialty_code=plan_data.specialty_code,
        )

        new_plan = await self.plan_repo.create_entity(plan)
        return new_plan

    async def _delete_plan(self, plan_id: int) -> bool:
        """Удаление учебного плана"""
        plan = await self._get_plan_by_id(plan_id)
        delete_result = await self.plan_repo.delete_entity(plan)
        return delete_result

    async def _update_plan(self, plan_id: int, plan_data: UpdatePlan) -> Plan:
        """Обновление учебного плана"""
        plan = await self._get_plan_by_id(plan_id)

        updated_data = plan_data.model_dump(exclude_unset=True)
        if "specialty_code" in updated_data:
            await self.specialty_service._get_specialty_by_code(updated_data["specialty_code"])

        for field, value in updated_data.items():
            setattr(plan, field, value)

        updated_plan = await self.plan_repo.update_entity(plan)
        return updated_plan
