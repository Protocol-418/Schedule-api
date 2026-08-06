from typing import Annotated

from fastapi import APIRouter, Depends

from app.src.plan.schemas import CreatePlan, ShowPlan, UpdatePlan
from app.src.plan.service import PlanService

plan_router = APIRouter(prefix="/plan", tags=["plans"])


@plan_router.post("/create", response_model=ShowPlan, status_code=201)
async def create_plan(
    body: CreatePlan,
    plan_service: Annotated[PlanService, Depends(PlanService)]
):
    return await plan_service._create_plan(body)


@plan_router.get("/search/by-id/{plan_id}", response_model=ShowPlan, status_code=200)
async def get_plan_by_id(
    plan_id: int,
    plan_service: Annotated[PlanService, Depends(PlanService)]
):
    return await plan_service._get_plan_by_id(plan_id)


@plan_router.get("/search/all", response_model=list[ShowPlan], status_code=200)
async def get_all_plans(
    plan_service: Annotated[PlanService, Depends(PlanService)]
):
    return await plan_service._get_all_plans()


@plan_router.get("/search/by-specialty/{specialty_code}", response_model=list[ShowPlan], status_code=200)
async def get_plans_by_specialty(
    specialty_code: str,
    plan_service: Annotated[PlanService, Depends(PlanService)]
):
    return await plan_service._get_plans_by_specialty(specialty_code)


@plan_router.delete("/delete/{plan_id}", response_model=bool, status_code=200)
async def delete_plan(
    plan_id: int,
    plan_service: Annotated[PlanService, Depends(PlanService)]
):
    return await plan_service._delete_plan(plan_id)


@plan_router.put("/update/{plan_id}", response_model=ShowPlan, status_code=200)
async def update_plan(
    plan_id: int,
    body: UpdatePlan,
    plan_service: Annotated[PlanService, Depends(PlanService)]
):
    return await plan_service._update_plan(plan_id, body)
