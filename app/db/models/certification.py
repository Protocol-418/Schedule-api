from sqlalchemy import BigInteger, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.models.base import Base


class Certification(Base):
    """Форма аттестации по дисциплине"""

    __tablename__ = "certifications"

    subject_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("subjects.id", onupdate="CASCADE"), primary_key=True
    )
    credit: Mapped[bool] = mapped_column(Boolean)
    differentiated_credit: Mapped[bool] = mapped_column(Boolean)
    course_project: Mapped[bool] = mapped_column(Boolean)
    course_work: Mapped[bool] = mapped_column(Boolean)
    control_work: Mapped[bool] = mapped_column(Boolean)
    other_form: Mapped[bool] = mapped_column(Boolean)

    # Relationships
    subject: Mapped["Subject"] = relationship(back_populates="certification")
