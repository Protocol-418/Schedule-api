from typing import Annotated

from fastapi import APIRouter, Depends

from app.src.speciality.schemas import CreateSpecialty, ShowSpecialty, UpdateSpecialty
from app.src.speciality.service import SpecialtyService

specialty_router = APIRouter(prefix="/specialty", tags=["specialties"])


@specialty_router.post("/create", response_model=ShowSpecialty, status_code=201)
async def create_specialty(
    body: CreateSpecialty,
    specialty_service: Annotated[SpecialtyService, Depends(SpecialtyService)]
):
    return await specialty_service._create_specialty(body)


@specialty_router.get("/search/by-code/{code}", response_model=ShowSpecialty, status_code=200)
async def get_specialty_by_code(
    code: str,
    specialty_service: Annotated[SpecialtyService, Depends(SpecialtyService)]
):
    return await specialty_service._get_specialty_by_code(code)


@specialty_router.get("/search/all", response_model=list[ShowSpecialty], status_code=200)
async def get_all_specialties(
    specialty_service: Annotated[SpecialtyService, Depends(SpecialtyService)]
):
    return await specialty_service._get_all_specialties()


@specialty_router.delete("/delete/{code}", response_model=bool, status_code=200)
async def delete_specialty(
    code: str,
    specialty_service: Annotated[SpecialtyService, Depends(SpecialtyService)]
):
    return await specialty_service._delete_specialty(code)


@specialty_router.put("/update/{code}", response_model=ShowSpecialty, status_code=200)
async def update_specialty(
    code: str,
    body: UpdateSpecialty,
    specialty_service: Annotated[SpecialtyService, Depends(SpecialtyService)]
):
    return await specialty_service._update_specialty(code, body)
