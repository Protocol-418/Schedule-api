from app.db.models.base import Base

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Boolean, String


class PaymentForm(Base):
    """Справочник форм оплаты"""
    __tablename__ = "payment_forms"

    name: Mapped[str] = mapped_column(String(50), primary_key=True)
    is_state_funded: Mapped[bool] = mapped_column(Boolean, nullable=False)

    # Relationships
    groups: Mapped[list["Group"]] = relationship(back_populates="payment_form_rel")