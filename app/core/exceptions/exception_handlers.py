# Файл с обработчиками ошибок в fast api
from app.core.exceptions.exceptions import AppBaseException
from fastapi import Request
from fastapi.responses import JSONResponse


async def app_exception_handler(request: Request, exc: AppBaseException):
    """Общий обработчик кастомных ошибок"""
    # Логирование внутренней информации (для мониторинга)
    # logger.error(f"[{exc.service}] {exc.error_code}: {exc.message}", extra={"details": exc.details})

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "code": exc.error_code,
                "message": exc.detail, 
                "service": exc.service,
                "details": exc.details
            }
        }
    )

