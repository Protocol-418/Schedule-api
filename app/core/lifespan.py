from contextlib import asynccontextmanager
from fastapi import FastAPI
import redis.asyncio as redis
from app.core.config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Создаём пул соединений
    pool = redis.ConnectionPool.from_url(
        settings.REDIS_SESSIONS_URL,
        decode_responses=True,
        max_connections=50,
        socket_timeout=1.0,         # Если редис за 1 сек не ответил — рвем коннект
        socket_connect_timeout=1.0  # Ограничение на время самого подключения
    )
    
    # Инициализируем клиент Redis, привязав его к пулу
    redis_client = redis.Redis(connection_pool=pool)
    
    # Сохраняем клиента в стейт приложения
    app.state.redis_client = redis_client

    yield

    # Закрываем все соединения при закрытии сервера
    await redis_client.aclose()
    await pool.disconnect()