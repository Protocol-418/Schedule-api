from app.db.models.base import Base
from app.db.mixins.id_mixin import IDMixin

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey


class Cabinet(IDMixin, Base):
    """Кабинеты"""
    __tablename__ = "cabinets"

    number: Mapped[int] = mapped_column(Integer)
    capacity: Mapped[int] = mapped_column(Integer)
    state: Mapped[str | None] = mapped_column(String(50))

    # Foreign keys
    building_number: Mapped[int] = mapped_column(Integer, ForeignKey("buildings.number", onupdate="CASCADE"))

    # Relationships
    building: Mapped["Building"] = relationship(back_populates="cabinets")
    class_sessions: Mapped[list["ClassSession"]] = relationship(back_populates="cabinet")
