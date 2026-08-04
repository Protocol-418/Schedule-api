import uuid
from typing import Annotated

import redis.asyncio as redis
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.dependies import get_db, get_redis_sessions
from app.core.exceptions.exceptions import Unauthorized
from app.core.security.password import verify_password
from app.src.auth.repository import UserSessionsRepository
from app.src.auth.schemas import LoginRequest
from app.src.user.repository import UserRepository


class AuthService:
    def __init__(
            self,
            session: Annotated[AsyncSession, Depends(get_db)],
            redis_sessions: Annotated[redis.Redis, Depends(get_redis_sessions)]
        ):
        self.session = session
        self.redis_sessions = redis_sessions
        self.user_repo = UserRepository(self.session)
        self.redis_sessions_repo = UserSessionsRepository(self.redis_sessions)

    async def _login_user(self, login_data: LoginRequest) -> str:
        """Авторизация пользователя в системе"""
        # Существует ли пользователь с таким email и верен ли пароль
        user = await self.user_repo.get_entity_by_filter(email=login_data.email)
        if not user or not verify_password(login_data.password, user.hashed_password):
            raise Unauthorized(service="Auth", message="Такого пользователя не существует или неверно указан пароль")
        
        # Готовим данные для создания сессии
        session_token = uuid.uuid4().hex
        session_data = {
            "user_uuid": str(user.uuid),
            "user_role": user.role
        }

        # Создаём сессию
        await self.redis_sessions_repo.save_session(
            session_token=session_token, 
            session_data=session_data
        )

        return session_token

    async def _get_user_session(self, session_token) -> dict:
        """Метод для получения сессии пользователя"""
        user_session_data = await self.redis_sessions_repo.get_session(session_token)
        if not user_session_data:
            raise Unauthorized(service="Auth", message="Время действия токена истекло или он не существует")
        
        return user_session_data
        


        
