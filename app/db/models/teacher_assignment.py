from app.db.models.base import Base

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import BigInteger, Integer, String, ForeignKey


class TeacherAssignment(Base):
    """Назначение преподавателя на дисциплину для группы"""
    __tablename__ = "teacher_assignments"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)

    # Foreign keys
    teacher_id: Mapped[int] = mapped_column(Integer, ForeignKey("teachers.id", onupdate="CASCADE"))
    subject_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("subjects.id", onupdate="CASCADE"))
    group_name: Mapped[str] = mapped_column(String(50), ForeignKey("groups.name", onupdate="CASCADE"))

    # Relationships
    teacher: Mapped["Teacher"] = relationship(back_populates="assignments")
    subject: Mapped["Subject"] = relationship(back_populates="assignments")
    group: Mapped["Group"] = relationship(back_populates="assignments")
    class_sessions: Mapped[list["ClassSession"]] = relationship(back_populates="assignment")