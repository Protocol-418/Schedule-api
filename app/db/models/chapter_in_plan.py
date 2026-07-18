from app.db.models.base import Base
from app.db.mixins.code_name_mixin import CodeNameMixin
from app.db.mixins.id_mixin import IDMixin

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey


class ChapterInPlan(IDMixin, CodeNameMixin, Base):
    """Раздел учебного плана"""
    __tablename__ = "chapter_in_plan"

    plan_id: Mapped[int] = mapped_column(Integer, ForeignKey("plans.id", onupdate="CASCADE"))

    # Relationships
    plan: Mapped["Plan"] = relationship(back_populates="chapters")
    cycles: Mapped[list["CycleInChapter"]] = relationship(back_populates="chapter")