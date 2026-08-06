from typing import Annotated

from fastapi import APIRouter, Depends

from app.src.class_session_type.schemas import (
    CreateClassSessionType,
    ShowClassSessionType,
    UpdateClassSessionType,
)
from app.src.class_session_type.service import ClassSessionTypeService

class_session_type_router = APIRouter(prefix="/class-session-type", tags=["class_session_types"])


@class_session_type_router.post("/create", response_model=ShowClassSessionType, status_code=201)
async def create_class_session_type(
    body: CreateClassSessionType,
    type_service: Annotated[ClassSessionTypeService, Depends(ClassSessionTypeService)]
):
    return await type_service._create_type(body)


@class_session_type_router.get("/search/by-name/{name}", response_model=ShowClassSessionType, status_code=200)
async def get_class_session_type_by_name(
    name: str,
    type_service: Annotated[ClassSessionTypeService, Depends(ClassSessionTypeService)]
):
    return await type_service._get_type_by_name(name)


@class_session_type_router.get("/search/all", response_model=list[ShowClassSessionType], status_code=200)
async def get_all_class_session_types(
    type_service: Annotated[ClassSessionTypeService, Depends(ClassSessionTypeService)]
):
    return await type_service._get_all_types()


@class_session_type_router.delete("/delete/{name}", response_model=bool, status_code=200)
async def delete_class_session_type(
    name: str,
    type_service: Annotated[ClassSessionTypeService, Depends(ClassSessionTypeService)]
):
    return await type_service._delete_type(name)


@class_session_type_router.put("/update/{name}", response_model=ShowClassSessionType, status_code=200)
async def update_class_session_type(
    name: str,
    body: UpdateClassSessionType,
    type_service: Annotated[ClassSessionTypeService, Depends(ClassSessionTypeService)]
):
    return await type_service._update_type(name, body)
