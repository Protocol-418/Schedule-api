import redis.asyncio as redis
from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.core.config import settings

# База данных
engine = create_async_engine(settings.DATABASE_URL, echo=True)
AsyncSession = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def get_db():
    """Функция для соединения с базой данных"""
    async with AsyncSession() as session:
        yield session


async def get_redis_sessions(request: Request) -> redis.Redis:
    """Функция для получения клиента Redis"""
    return request.app.state.redis_client
