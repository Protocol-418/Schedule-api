from app.main_router import main_router

from app.core.lifespan import lifespan

from app.core.exceptions.exception_handlers import app_exception_handler
from app.core.exceptions.exceptions import AppBaseException

import uvicorn
from fastapi import FastAPI

app = FastAPI(lifespan=lifespan) # Создаём экземпляр приложения и добавляем соединение с redis в жизненный цикл
app.include_router(main_router) # Подключаем main роутер, в котором все остальные 
app.add_exception_handler(AppBaseException, app_exception_handler) # Подключаем главный обработчик ошибок


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)