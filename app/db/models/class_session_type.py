from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.models.base import Base


class ClassSessionType(Base):
    """Справочник типов занятий"""

    __tablename__ = "class_session_types"

    name: Mapped[str] = mapped_column(String(50), primary_key=True)

    # Relationships
    class_sessions: Mapped[list["ClassSession"]] = relationship(
        back_populates="session_type"
    )
