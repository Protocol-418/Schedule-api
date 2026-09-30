from typing import Annotated

from fastapi import APIRouter, Depends

from app.core.base_schemas import Pagination
from app.src.teacher_category.schemas import (
    CreateTeacherCategory,
    ShowTeacherCategory,
    UpdateTeacherCategory,
)
from app.src.teacher_category.service import TeacherCategoryService

teacher_category_router = APIRouter(prefix="/teacher-category", tags=["teacher-categories"])


@teacher_category_router.post("/create", response_model=ShowTeacherCategory, status_code=201)
async def create_category(
    body: CreateTeacherCategory,
    category_service: Annotated[TeacherCategoryService, Depends(TeacherCategoryService)]
):
    return await category_service._create_category(body)


@teacher_category_router.get("/search/by-name/{name}", response_model=ShowTeacherCategory, status_code=200)
async def get_category_by_name(
    name: str,
    category_service: Annotated[TeacherCategoryService, Depends(TeacherCategoryService)]
):
    return await category_service._get_category_by_name(name)


@teacher_category_router.get("/search/all", response_model=list[ShowTeacherCategory], status_code=200)
async def get_all_categories(
    category_service: Annotated[TeacherCategoryService, Depends(TeacherCategoryService)],
    pagination: Annotated[Pagination, Depends()],
):
    return await category_service._get_all_categories(pagination)


@teacher_category_router.delete("/delete/{name}", response_model=bool, status_code=200)
async def delete_category(
    name: str,
    category_service: Annotated[TeacherCategoryService, Depends(TeacherCategoryService)]
):
    return await category_service._delete_category(name)


@teacher_category_router.put("/update/{name}", response_model=ShowTeacherCategory, status_code=200)
async def update_category(
    name: str,
    body: UpdateTeacherCategory,
    category_service: Annotated[TeacherCategoryService, Depends(TeacherCategoryService)]
):
    return await category_service._update_category(name, body)