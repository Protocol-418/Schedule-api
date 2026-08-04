import json

import redis.asyncio as redis


class UserSessionsRepository:
    def __init__(self, redis_session: redis.Redis):
        # Сохраняем клиент в self.session
        self.session = redis_session

    async def save_session(
        self, session_token: str, session_data: dict, ttl_seconds: int = 2592000
    ) -> None:
        """Метод для сохранения сессии пользователя в redis"""
        await self.session.set(
            name=f"session:{session_token}",
            value=json.dumps(session_data),
            ex=ttl_seconds,  # По умолчанию 30 дней
        )

    async def get_session(self, session_token: str) -> dict | None:
        """Получить данные сессии из Redis"""
        raw_data = await self.session.get(f"session:{session_token}")
        if not raw_data:
            return None
        return json.loads(raw_data)
