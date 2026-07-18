from app.db.models.base import Base

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import BigInteger, String, Integer, ForeignKey


class Stream(Base):
    """Поток (объединение нескольких групп по дисциплине)"""
    __tablename__ = "streams"

    number: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str | None] = mapped_column(String(255))

    # Foreign keys
    group_id: Mapped[int] = mapped_column(
        String(50),
        ForeignKey("groups.name", onupdate="CASCADE"),
        primary_key=True
    )
    subject_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("subjects.id", onupdate="CASCADE"),
        primary_key=True
    )

    # Relationships
    group: Mapped["Group"] = relationship(back_populates="streams")
    subject: Mapped["Subject"] = relationship(back_populates="streams")