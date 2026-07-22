from fastapi import APIRouter
from app.src.user.router import user_router
from app.src.auth.router import auth_router
from app.src.teacher.router import teacher_router
from app.src.teacher_category.router import teacher_category_router
from app.src.payment_form.router import payment_form_router

main_router = APIRouter()
main_router.include_router(user_router)
main_router.include_router(auth_router)
main_router.include_router(teacher_router)
main_router.include_router(teacher_category_router)
main_router.include_router(payment_form_router)

