from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.mixins.code_name_mixin import CodeNameMixin
from app.db.mixins.id_mixin import IDMixin
from app.db.models.base import Base


class ModuleInCycle(IDMixin, CodeNameMixin, Base):
    """Модуль в цикле"""

    __tablename__ = "module_in_cycle"

    cycle_in_chapter_id: Mapped[int | None] = mapped_column(
        Integer, ForeignKey("cycle_in_chapter.id", onupdate="CASCADE")
    )

    # Relationships
    cycle: Mapped["CycleInChapter"] = relationship(back_populates="modules")
