from app.core.base_repository import BaseRepository
from app.db.models.payment_form import PaymentForm


class PaymentFormRepository(BaseRepository):
    model = PaymentForm
