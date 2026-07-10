from app.db.models.user import User
from app.src.user.service import UserService
from app.src.user.schemas import CreateUser, ShowUser, UpdateUser
from app.core.security.security import RoleChecker

from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends

user_router = APIRouter(prefix="/user", tags=["users"])


@user_router.post("/register", response_model=ShowUser, status_code=200)
async def create_user(
    body: CreateUser,
    user_service: Annotated[UserService, Depends(UserService)]
):
    return await user_service._create_user(body)


@user_router.get("/search/by-uuid/{user_uuid}", response_model=ShowUser, status_code=200)
async def get_user_by_uuid(
    user_uuid: UUID, 
    user_service: Annotated[UserService, Depends(UserService)],
    current_user: Annotated[User, Depends(RoleChecker(["admin"]))]
):
    return await user_service._get_user_by_uuid(user_uuid)


@user_router.get("/search/all", response_model=list[ShowUser], status_code=200)
async def get_all_users(
    user_service: Annotated[UserService, Depends(UserService)],
    current_user: Annotated[User, Depends(RoleChecker(["admin"]))]
):
    return await user_service._get_all_users()


@user_router.get("/search/by-role/{role}", response_model=list[ShowUser], status_code=200)
async def get_users_by_role(
    role: str,
    user_service: Annotated[UserService, Depends(UserService)],
    current_user: Annotated[User, Depends(RoleChecker(["admin"]))]
):
    return await user_service._get_users_by_role(role)


@user_router.delete("/delete/{uuid}", response_model=bool, status_code=200)
async def delete_user(
    uuid: UUID,
    user_service: Annotated[UserService, Depends(UserService)],
    current_user: Annotated[User, Depends(RoleChecker(["admin"]))]
):
    return await user_service._delete_user(uuid)


@user_router.put("/update/{uuid}", response_model=ShowUser, status_code=200)
async def update_user(
    uuid: UUID,
    body: UpdateUser,
    user_service: Annotated[UserService, Depends(UserService)],
    current_user: Annotated[User, Depends(RoleChecker(["admin"]))]
):
    return await user_service._update_user(uuid, body)