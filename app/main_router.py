from fastapi import APIRouter

from app.src.auth.router import auth_router
from app.src.building.router import building_router
from app.src.cabinet.router import cabinet_router
from app.src.certification.router import certification_router
from app.src.class_session_type.router import class_session_type_router
from app.src.group.router import group_router
from app.src.payment_form.router import payment_form_router
from app.src.plan.router import plan_router
from app.src.speciality.router import specialty_router
from app.src.teacher.router import teacher_router
from app.src.teacher_category.router import teacher_category_router
from app.src.user.router import user_router

main_router = APIRouter()
main_router.include_router(user_router)
main_router.include_router(auth_router)
main_router.include_router(teacher_router)
main_router.include_router(teacher_category_router)
main_router.include_router(payment_form_router)
main_router.include_router(specialty_router)
main_router.include_router(building_router)
main_router.include_router(cabinet_router)
main_router.include_router(certification_router)
main_router.include_router(class_session_type_router)
main_router.include_router(group_router)
main_router.include_router(plan_router)
