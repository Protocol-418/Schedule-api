from app.db.models.base import Base

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey, UniqueConstraint


class Group(Base):
    """Учебная группа"""
    __tablename__ = "groups"

    name: Mapped[str] = mapped_column(String(50), primary_key=True)
    year_admission: Mapped[int] = mapped_column(Integer)
    count_students: Mapped[int] = mapped_column(Integer)

    # Foreign keys
    group_advisor_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("teachers.id", onupdate="CASCADE"))
    specialty_code: Mapped[str] = mapped_column(String(20), ForeignKey("specialties.code", onupdate="CASCADE"))
    payment_form: Mapped[str] = mapped_column(String(50), ForeignKey("payment_forms.name", onupdate="CASCADE"))

    # Relationships
    advisor: Mapped["Teacher"] = relationship(back_populates="advised_groups")
    specialty: Mapped["Specialty"] = relationship(back_populates="groups")
    payment_form_rel: Mapped["PaymentForm"] = relationship(back_populates="groups")
    assignments: Mapped[list["TeacherAssignment"]] = relationship(back_populates="group")
    streams: Mapped[list["Stream"]] = relationship(back_populates="group")