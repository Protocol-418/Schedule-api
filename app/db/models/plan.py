from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.mixins.id_mixin import IDMixin
from app.db.models.base import Base


class Plan(IDMixin, Base):
    """Учебный план"""

    __tablename__ = "plans"

    year: Mapped[int] = mapped_column(Integer)

    # Foreign keys
    specialty_code: Mapped[str] = mapped_column(
        String(20), ForeignKey("specialties.code", onupdate="CASCADE")
    )

    # Relationships
    specialty: Mapped["Specialty"] = relationship(back_populates="plans")
    semesters: Mapped[list["Semester"]] = relationship(back_populates="plan")
    chapters: Mapped[list["ChapterInPlan"]] = relationship(back_populates="plan")
