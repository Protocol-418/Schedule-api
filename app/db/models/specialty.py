from app.db.models.base import Base

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String


class Specialty(Base):
    """Справочник специальностей"""
    __tablename__ = "specialties"

    code: Mapped[str] = mapped_column(String(20), primary_key=True)
    title: Mapped[str | None] = mapped_column(String(255))

    # Relationships
    groups: Mapped[list["Group"]] = relationship(back_populates="specialty")
    plans: Mapped[list["Plan"]] = relationship(back_populates="specialty")