from app.db.models.base import Base
from app.db.mixins.id_mixin import IDMixin

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, Numeric, ForeignKey


class Semester(IDMixin, Base):
    """Семестр"""
    __tablename__ = "semesters"

    semester_number: Mapped[int] = mapped_column(Integer)
    weeks: Mapped[float] = mapped_column(Numeric)
    practice_weeks: Mapped[float] = mapped_column(Numeric)

    # Foreign keys
    plan_id: Mapped[int] = mapped_column(Integer, ForeignKey("plans.id", onupdate="CASCADE"))

    # Relationships
    plan: Mapped["Plan"] = relationship(back_populates="semesters")
    subjects: Mapped[list["Subject"]] = relationship(back_populates="semester")