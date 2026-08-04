from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.mixins.uuid_mixin import UUIDMixin
from app.db.models.base import Base


class User(UUIDMixin, Base):
    """Сущность пользователи"""

    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String(50), index=True, nullable=True)
    email: Mapped[str] = mapped_column(
        String(50), index=True, unique=True, nullable=False
    )
    role: Mapped[str] = mapped_column(String(25), nullable=False, default="admin")
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
