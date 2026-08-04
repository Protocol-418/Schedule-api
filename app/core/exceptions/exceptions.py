# Файл с описанием классов кастомных ошибок
from typing import Any

from fastapi import HTTPException


class AppBaseException(HTTPException):
    """Базовый класс для кастомных API-ошибок"""

    def __init__(
        self,
        status_code: int,
        error_code: str,
        message: str,
        service: str = "unknown",
        details: dict[str, Any] | None = None,
    ):
        super().__init__(status_code=status_code, detail=message)
        self.error_code = error_code
        self.service = service
        self.details = details or {}


class NotFoundException(AppBaseException):
    """Класс для не найденных объектов"""

    def __init__(self, message: str | None = None, service: str = "general"):
        super().__init__(
            status_code=404,
            error_code="RESOURCE_NOT_FOUND",
            message=message
            or "Ресурс не найден: проверьте корректность переданных данных",
            service=service,
        )


class ConflictException(AppBaseException):
    def __init__(self, message: str | None = None, service: str = "general"):
        super().__init__(
            status_code=409,
            error_code="EMAIL_ALREADY_EXISTS",
            message=message or "Пользователь с таким email уже зарегистрирован",
            service=service,
        )


class Unauthorized(AppBaseException):
    def __init__(self, message: str | None = None, service: str = "general"):
        super().__init__(
            status_code=401,
            error_code="UNAUTHORIZED",
            message=message
            or "Вы не были распознаны системой, проверьте входные данные",
            service=service,
        )


class Forbidden(AppBaseException):
    def __init__(self, message: str | None = None, service: str = "general"):
        super().__init__(
            status_code=403,
            error_code="FORBIDDEN",
            message=message or "Вам отказано в доступе",
            service=service,
        )
