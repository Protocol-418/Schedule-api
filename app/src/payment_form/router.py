from app.src.payment_form.service import PaymentFormService
from app.src.payment_form.schemas import CreatePaymentForm, ShowPaymentForm, UpdatePaymentForm

from typing import Annotated

from fastapi import APIRouter, Depends

payment_form_router = APIRouter(prefix="/payment-form", tags=["payment_forms"])


@payment_form_router.post("/create", response_model=ShowPaymentForm, status_code=201)
async def create_payment_form(
    body: CreatePaymentForm,
    payment_form_service: Annotated[PaymentFormService, Depends(PaymentFormService)]
):
    return await payment_form_service._create_payment_form(body)


@payment_form_router.get("/search/by-name/{name}", response_model=ShowPaymentForm, status_code=200)
async def get_payment_form_by_name(
    name: str,
    payment_form_service: Annotated[PaymentFormService, Depends(PaymentFormService)]
):
    return await payment_form_service._get_payment_form_by_name(name)


@payment_form_router.get("/search/all", response_model=list[ShowPaymentForm], status_code=200)
async def get_all_payment_forms(
    payment_form_service: Annotated[PaymentFormService, Depends(PaymentFormService)]
):
    return await payment_form_service._get_all_payment_forms()


@payment_form_router.delete("/delete/{name}", response_model=bool, status_code=200)
async def delete_payment_form(
    name: str,
    payment_form_service: Annotated[PaymentFormService, Depends(PaymentFormService)]
):
    return await payment_form_service._delete_payment_form(name)


@payment_form_router.put("/update/{name}", response_model=ShowPaymentForm, status_code=200)
async def update_payment_form(
    name: str,
    body: UpdatePaymentForm,
    payment_form_service: Annotated[PaymentFormService, Depends(PaymentFormService)]
):
    return await payment_form_service._update_payment_form(name, body)
