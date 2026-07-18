from app.db.models.base import Base
from app.db.mixins.code_name_mixin import CodeNameMixin
from app.db.mixins.id_mixin import IDMixin

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Boolean, Integer, ForeignKey


class CycleInChapter(IDMixin, CodeNameMixin, Base):
    """Цикл в разделе плана"""
    __tablename__ = "cycle_in_chapter"

    contains_modules: Mapped[bool] = mapped_column(Boolean)
    
    # Foreign keys
    chapter_in_plan_id: Mapped[int] = mapped_column(Integer, ForeignKey("chapter_in_plan.id", onupdate="CASCADE"))

    # Relationships
    chapter: Mapped["ChapterInPlan"] = relationship(back_populates="cycles")
    modules: Mapped[list["ModuleInCycle"]] = relationship(back_populates="cycle")