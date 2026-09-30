from typing import Annotated

from fastapi import APIRouter, Depends

from app.core.base_schemas import Pagination
from app.src.certification.schemas import (
    CreateCertification,
    ShowCertification,
    UpdateCertification,
)
from app.src.certification.service import CertificationService

certification_router = APIRouter(prefix="/certification", tags=["certifications"])


@certification_router.post("/create", response_model=ShowCertification, status_code=201)
async def create_certification(
    body: CreateCertification,
    certification_service: Annotated[CertificationService, Depends(CertificationService)]
):
    return await certification_service._create_certification(body)


@certification_router.get("/search/by-subject-id/{subject_id}", response_model=ShowCertification, status_code=200)
async def get_certification_by_subject_id(
    subject_id: int,
    certification_service: Annotated[CertificationService, Depends(CertificationService)]
):
    return await certification_service._get_certification_by_subject_id(subject_id)


@certification_router.get("/search/all", response_model=list[ShowCertification], status_code=200)
async def get_all_certifications(
    certification_service: Annotated[CertificationService, Depends(CertificationService)],
    pagination: Annotated[Pagination, Depends()],
):
    return await certification_service._get_all_certifications(pagination)


@certification_router.delete("/delete/{subject_id}", response_model=bool, status_code=200)
async def delete_certification(
    subject_id: int,
    certification_service: Annotated[CertificationService, Depends(CertificationService)]
):
    return await certification_service._delete_certification(subject_id)


@certification_router.put("/update/{subject_id}", response_model=ShowCertification, status_code=200)
async def update_certification(
    subject_id: int,
    body: UpdateCertification,
    certification_service: Annotated[CertificationService, Depends(CertificationService)]
):
    return await certification_service._update_certification(subject_id, body)
