from app.db.models.base import Base

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey


class Teacher(Base):
    """Преподаватель"""
    __tablename__ = "teachers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100))
    surname: Mapped[str] = mapped_column(String(100))
    lastname: Mapped[str | None] = mapped_column(String(100))
    phone_number: Mapped[str | None] = mapped_column(String(20))
    email: Mapped[str | None] = mapped_column(String(100))

    # Foreign keys
    teacher_category: Mapped[str | None] = mapped_column(String(50), ForeignKey("teachers_categories.name", onupdate="CASCADE"))

    # Relationships
    category: Mapped["TeachersCategory"] = relationship(back_populates="teachers")
    advised_groups: Mapped[list["Group"]] = relationship(back_populates="advisor")
    assignments: Mapped[list["TeacherAssignment"]] = relationship(back_populates="teacher")