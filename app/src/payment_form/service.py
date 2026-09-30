from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.base_schemas import Pagination
from app.core.dependies import get_db
from app.core.exceptions.exceptions import NotFoundException
from app.db.models.payment_form import PaymentForm
from app.src.payment_form.repository import PaymentFormRepository
from app.src.payment_form.schemas import CreatePaymentForm, UpdatePaymentForm


class PaymentFormService:
    def __init__(self, session: Annotated[AsyncSession, Depends(get_db)]):
        self.session = session
        self.payment_form_repo = PaymentFormRepository(self.session)

    async def _get_payment_form_by_name(self, name: str) -> PaymentForm:
        """Получение формы оплаты по названию"""
        payment_form = await self.payment_form_repo.get_entity_by_filter(name=name)
        if not payment_form:
            raise NotFoundException(service="PaymentForm", message="Форма оплаты с таким названием не найдена")
        return payment_form

    async def _get_all_payment_forms(self, pagination: Pagination) -> list[PaymentForm]:
        """Получение всех форм оплаты"""
        payment_forms = await self.payment_form_repo.get_all_entities(pagination=pagination)
        return payment_forms

    async def _create_payment_form(self, payment_form_data: CreatePaymentForm) -> PaymentForm:
        """Создание новой формы оплаты"""
        payment_form = PaymentForm(
            name=payment_form_data.name,
            is_state_funded=payment_form_data.is_state_funded
        )

        new_payment_form = await self.payment_form_repo.create_entity(payment_form)
        return new_payment_form

    async def _delete_payment_form(self, name: str) -> bool:
        """Удаление формы оплаты"""
        payment_form = await self._get_payment_form_by_name(name)
        delete_result = await self.payment_form_repo.delete_entity(payment_form)
        return delete_result

    async def _update_payment_form(self, name: str, payment_form_data: UpdatePaymentForm) -> PaymentForm:
        """Обновление формы оплаты"""
        payment_form = await self._get_payment_form_by_name(name)

        updated_payment_form_data = payment_form_data.model_dump(exclude_unset=True)
        for field, value in updated_payment_form_data.items():
            setattr(payment_form, field, value)

        updated_payment_form = await self.payment_form_repo.update_entity(payment_form)
        return updated_payment_form
