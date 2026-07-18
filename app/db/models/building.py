from app.db.models.base import Base

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Boolean


class Building(Base):
    """Корпуса"""
    __tablename__ = "buildings"

    number: Mapped[int] = mapped_column(Integer, primary_key=True)
    city: Mapped[str | None] = mapped_column(String(100))
    address: Mapped[str | None] = mapped_column(String(255))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    # Relationships
    cabinets: Mapped[list["Cabinet"]] = relationship(back_populates="building")