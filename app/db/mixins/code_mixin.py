from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String


class CodeMixin:
    code: Mapped[str] = mapped_column(String(30))