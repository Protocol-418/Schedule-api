from app.db.models.base import Base
from app.db.mixins.id_mixin import IDMixin

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Date, ForeignKey, BigInteger


class ClassSession(IDMixin, Base):
    """Занятие в расписании"""
    __tablename__ = "class_sessions"

    number: Mapped[int] = mapped_column(Integer)
    date: Mapped[Date] = mapped_column(Date)

    # Foreign keys
    teacher_assignment_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("teacher_assignments.id", onupdate="CASCADE"))
    cabinet_id: Mapped[int] = mapped_column(Integer, ForeignKey("cabinets.id", onupdate="CASCADE"))
    class_session_type: Mapped[str] = mapped_column(String(50), ForeignKey("class_session_types.name", onupdate="CASCADE"))

    # Relationships
    assignment: Mapped["TeacherAssignment"] = relationship(back_populates="class_sessions")
    cabinet: Mapped["Cabinet"] = relationship(back_populates="class_sessions")
    session_type: Mapped["ClassSessionType"] = relationship(back_populates="class_sessions")