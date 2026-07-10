from fastapi import APIRouter
from app.src.user.router import user_router
from app.src.auth.router import auth_router

main_router = APIRouter()
main_router.include_router(user_router)
main_router.include_router(auth_router)

