from typing import Annotated

from fastapi import Depends, Request

from app.core.exceptions.exceptions import Forbidden, Unauthorized
from app.db.models.user import User
from app.src.auth.service import AuthService
from app.src.user.service import UserService


async def get_current_user(
    request: Request,
    auth_service: Annotated[AuthService, Depends(AuthService)],
    user_service: Annotated[UserService, Depends(UserService)]
) -> User:
    session_token = request.cookies.get("session_token")
    if not session_token:
        raise Unauthorized(service="Auth", message="Токен не передан")
        
    user_session = await auth_service._get_user_session(session_token)
    user = await user_service._get_user_by_uuid(user_session.get("user_uuid"))

    return user


class RoleChecker:
    def __init__(self, allowed_roles: list[str]):
        # Сохраняем список ролей, которым разрешен доступ
        self.allowed_roles = allowed_roles

    async def __call__(self, current_user: Annotated[User, Depends(get_current_user)]) -> User:
        # Проверяем роль пользователя 
        if current_user.role not in self.allowed_roles:
            raise Forbidden(service="Auth", message="Для вашей роли доступ запрещён")
            
        # Если всё ок - возвращаем пользователя в эндпоинт
        return current_user

        
    
