from app.db.models.base import Base

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String


class TeachersCategory(Base):
    """Категория преподавателей"""
    __tablename__ = "teachers_categories"

    name: Mapped[str] = mapped_column(String(50), primary_key=True)
    
    # Relationships
    teachers: Mapped[list["Teacher"]] = relationship(back_populates="category")