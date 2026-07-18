from app.db.models.base import Base

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import BigInteger, String, Boolean, Integer, ForeignKey


class Subject(Base):
    """Дисциплина"""
    __tablename__ = "subjects"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    code: Mapped[str] = mapped_column(String(20))
    name: Mapped[str] = mapped_column(String(255))
    alias: Mapped[str | None] = mapped_column(String(255))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    self_study_hours: Mapped[int] = mapped_column(Integer)
    lectures_hours: Mapped[int] = mapped_column(Integer)
    laboratory_hours: Mapped[int] = mapped_column(Integer)
    practical_hours: Mapped[int] = mapped_column(Integer)
    course_project_hours: Mapped[int] = mapped_column(Integer)
    consultation_hours: Mapped[int] = mapped_column(Integer)
    intermediate_assessment_hours: Mapped[int] = mapped_column(Integer)

    # Foreign keys
    semester_id: Mapped[int] = mapped_column(Integer, ForeignKey("semesters.id", onupdate="CASCADE"))

    # Relationships
    semester: Mapped["Semester"] = relationship(back_populates="subjects")
    certification: Mapped["Certification"] = relationship(back_populates="subject")
    assignments: Mapped[list["TeacherAssignment"]] = relationship(back_populates="subject")
    streams: Mapped[list["Stream"]] = relationship(back_populates="subject")