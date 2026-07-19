from app.src.teacher.service import TeacherService
from app.src.teacher.schemas import CreateTeacher, ShowTeacher, UpdateTeacher

from typing import Annotated

from fastapi import APIRouter, Depends

teacher_router = APIRouter(prefix="/teacher", tags=["teachers"])


@teacher_router.post("/create", response_model=ShowTeacher, status_code=201)
async def create_teacher(
    body: CreateTeacher,
    teacher_service: Annotated[TeacherService, Depends(TeacherService)]
):
    return await teacher_service._create_teacher(body)


@teacher_router.get("/search/by-id/{teacher_id}", response_model=ShowTeacher, status_code=200)
async def get_teacher_by_id(
    teacher_id: int,
    teacher_service: Annotated[TeacherService, Depends(TeacherService)]
):
    return await teacher_service._get_teacher_by_id(teacher_id)


@teacher_router.get("/search/all", response_model=list[ShowTeacher], status_code=200)
async def get_all_teachers(
    teacher_service: Annotated[TeacherService, Depends(TeacherService)]
):
    return await teacher_service._get_all_teachers()


@teacher_router.delete("/delete/{teacher_id}", response_model=bool, status_code=200)
async def delete_teacher(
    teacher_id: int,
    teacher_service: Annotated[TeacherService, Depends(TeacherService)]
):
    return await teacher_service._delete_teacher(teacher_id)


@teacher_router.put("/update/{teacher_id}", response_model=ShowTeacher, status_code=200)
async def update_teacher(
    teacher_id: int,
    body: UpdateTeacher,
    teacher_service: Annotated[TeacherService, Depends(TeacherService)]
):
    return await teacher_service._update_teacher(teacher_id, body)


@teacher_router.patch("/clear-category/{teacher_id}", response_model=ShowTeacher, status_code=200)
async def clear_category(
    teacher_id: int,
    teacher_service: Annotated[TeacherService, Depends(TeacherService)]
):
    return await teacher_service._clear_category(teacher_id)