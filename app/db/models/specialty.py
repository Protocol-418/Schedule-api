from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.models.base import Base


class Specialty(Base):
    """Справочник специальностей"""

    __tablename__ = "specialties"

    code: Mapped[str] = mapped_column(String(20), primary_key=True)
    title: Mapped[str | None] = mapped_column(String(255))

    # Relationships
    groups: Mapped[list["Group"]] = relationship(back_populates="specialty")
    plans: Mapped[list["Plan"]] = relationship(back_populates="specialty")
