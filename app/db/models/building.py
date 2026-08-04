from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.models.base import Base


class Building(Base):
    """Корпуса"""

    __tablename__ = "buildings"

    number: Mapped[int] = mapped_column(Integer, primary_key=True)
    city: Mapped[str | None] = mapped_column(String(100))
    address: Mapped[str | None] = mapped_column(String(255))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    # Relationships
    cabinets: Mapped[list["Cabinet"]] = relationship(back_populates="building")
