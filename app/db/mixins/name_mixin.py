from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String


class NameMixin:
    name: Mapped[str] = mapped_column(String(255))