from typing import Annotated

from fastapi import APIRouter, Depends

from app.core.base_schemas import Pagination
from app.src.group.schemas import CreateGroup, ShowGroup, UpdateGroup
from app.src.group.service import GroupService

group_router = APIRouter(prefix="/group", tags=["groups"])


@group_router.post("/create", response_model=ShowGroup, status_code=201)
async def create_group(
    body: CreateGroup,
    group_service: Annotated[GroupService, Depends(GroupService)]
):
    return await group_service._create_group(body)


@group_router.get("/search/by-name/{name}", response_model=ShowGroup, status_code=200)
async def get_group_by_name(
    name: str,
    group_service: Annotated[GroupService, Depends(GroupService)]
):
    return await group_service._get_group_by_name(name)


@group_router.get("/search/all", response_model=list[ShowGroup], status_code=200)
async def get_all_groups(
    group_service: Annotated[GroupService, Depends(GroupService)],
    pagination: Annotated[Pagination, Depends()],
):
    return await group_service._get_all_groups(pagination)


@group_router.get("/search/by-specialty/{specialty_code}", response_model=list[ShowGroup], status_code=200)
async def get_groups_by_specialty(
    specialty_code: str,
    group_service: Annotated[GroupService, Depends(GroupService)],
    pagination: Annotated[Pagination, Depends()],
):
    return await group_service._get_groups_by_specialty(specialty_code, pagination)


@group_router.delete("/delete/{name}", response_model=bool, status_code=200)
async def delete_group(
    name: str,
    group_service: Annotated[GroupService, Depends(GroupService)]
):
    return await group_service._delete_group(name)


@group_router.put("/update/{name}", response_model=ShowGroup, status_code=200)
async def update_group(
    name: str,
    body: UpdateGroup,
    group_service: Annotated[GroupService, Depends(GroupService)]
):
    return await group_service._update_group(name, body)
