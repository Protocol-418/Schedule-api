import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.exceptions.exception_handlers import app_exception_handler
from app.core.exceptions.exceptions import AppBaseException
from app.core.lifespan import lifespan
from app.main_router import main_router

app = FastAPI(
    lifespan=lifespan
)  # Создаём экземпляр приложения и добавляем соединение с redis в жизненный цикл
app.include_router(main_router)  # Подключаем main роутер, в котором все остальные
app.add_exception_handler(
    AppBaseException, app_exception_handler
)  # Подключаем главный обработчик ошибок

# Добавляем правила корс, чтобы фронт мог слать запросы на сервер.
# ОСТОРОЖНО, ТОЛЬКО ДЛЯ ЛОКАЛЬНОЙ РАЗРАБОТКИ!!!!
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешает запросы с любого порта и домена
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
