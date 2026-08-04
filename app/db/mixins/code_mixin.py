from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class CodeMixin:
    code: Mapped[str] = mapped_column(String(30))
