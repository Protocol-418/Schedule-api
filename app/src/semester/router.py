from typing import Annotated

from fastapi import APIRouter, Depends

from app.src.semester.schemas import CreateSemester, ShowSemester, UpdateSemester
from app.src.semester.service import SemesterService

semester_router = APIRouter(prefix="/semester", tags=["semesters"])


@semester_router.post("/create", response_model=ShowSemester, status_code=201)
async def create_semester(
    body: CreateSemester,
    semester_service: Annotated[SemesterService, Depends(SemesterService)]
):
    return await semester_service._create_semester(body)


@semester_router.get("/search/by-id/{semester_id}", response_model=ShowSemester, status_code=200)
async def get_semester_by_id(
    semester_id: int,
    semester_service: Annotated[SemesterService, Depends(SemesterService)]
):
    return await semester_service._get_semester_by_id(semester_id)


@semester_router.get("/search/all", response_model=list[ShowSemester], status_code=200)
async def get_all_semesters(
    semester_service: Annotated[SemesterService, Depends(SemesterService)]
):
    return await semester_service._get_all_semesters()


@semester_router.get("/search/by-plan/{plan_id}", response_model=list[ShowSemester], status_code=200)
async def get_semesters_by_plan(
    plan_id: int,
    semester_service: Annotated[SemesterService, Depends(SemesterService)]
):
    return await semester_service._get_semesters_by_plan(plan_id)


@semester_router.delete("/delete/{semester_id}", response_model=bool, status_code=200)
async def delete_semester(
    semester_id: int,
    semester_service: Annotated[SemesterService, Depends(SemesterService)]
):
    return await semester_service._delete_semester(semester_id)


@semester_router.put("/update/{semester_id}", response_model=ShowSemester, status_code=200)
async def update_semester(
    semester_id: int,
    body: UpdateSemester,
    semester_service: Annotated[SemesterService, Depends(SemesterService)]
):
    return await semester_service._update_semester(semester_id, body)
