from app.db.models import User

from app.src.auth.service import AuthService
from app.src.auth.schemas import LoginRequest

from typing import Annotated
from fastapi import APIRouter, Depends, Response
from app.core.security.security import get_current_user

auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.post("/login", status_code=200)
async def login_user(
    body: LoginRequest,
    response: Response,
    auth_service: Annotated[AuthService, Depends(AuthService)]
):
    session_token = await auth_service._login_user(body)

    # Записываем токен в куки
    response.set_cookie(
        key="session_token",
        value=session_token,
        httponly=True,     # Защита от XSS
        secure=False,       # Передача только по HTTPS, в прод TRUE!
        samesite="lax",    # Защита от CSRF-атак
        max_age=2592000    # 30 дней
    )
    
    return {"status": "success", "message": "Successfully logged in"}


@auth_router.post("/check", status_code=200)
async def check_user(
    auth_service: Annotated[AuthService, Depends(AuthService)],
    current_user: Annotated[User, Depends(get_current_user)]
):
    print(current_user)
    return current_user



