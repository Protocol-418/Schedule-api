from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Класс настроек переменных"""

    # База данных
    DB_CONTAINER_NAME: str = Field(env="DB_CONTAINER_NAME")
    DB_NAME: str = Field(env="DB_NAME")
    DB_PORT: int = Field(env="DB_PORT")
    DB_USER: str = Field(env="DB_USER")
    DB_PASS: str = Field(env="DB_PASS")

    # Redis для сессий пользователей
    REDIS_PASSWORD: str = Field(env="REDIS_PASSWORD")
    REDIS_SESSIONS_PORT: str = Field(env="REDIS_SESSIONS_PORT")

    @property
    def DATABASE_URL(self):
        """Функция возвращающая строку подключения для asyncpg"""
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@127.0.0.1:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def ALEMBIC_DATABASE_URL(self):
        """Функция возвращающая строку подключения для алембик (синхронный движок)"""
        return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASS}@127.0.0.1:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def REDIS_SESSIONS_URL(self):
        """Функция возвращающая строку подключения к редису (сессии пользователей)"""
        return f"redis://:{self.REDIS_PASSWORD}@127.0.0.1:{self.REDIS_SESSIONS_PORT}"

    model_config = SettingsConfigDict(
        env_file=".env",  # Указываем откуда читать env переменные
        extra="ignore",  # Указываем, что нужно игнорировать env переменные, которые мы не получили в классе
    )


settings = Settings()
