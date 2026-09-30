from typing import Annotated

from fastapi import APIRouter, Depends

from app.core.base_schemas import Pagination
from app.src.cabinet.schemas import CreateCabinet, ShowCabinet, UpdateCabinet
from app.src.cabinet.service import CabinetService

cabinet_router = APIRouter(prefix="/cabinet", tags=["cabinets"])


@cabinet_router.post("/create", response_model=ShowCabinet, status_code=201)
async def create_cabinet(
    body: CreateCabinet,
    cabinet_service: Annotated[CabinetService, Depends(CabinetService)],
):
    return await cabinet_service._create_cabinet(body)


@cabinet_router.get(
    "/search/by-id/{cabinet_id}", response_model=ShowCabinet, status_code=200
)
async def get_cabinet_by_id(
    cabinet_id: int, cabinet_service: Annotated[CabinetService, Depends(CabinetService)]
):
    return await cabinet_service._get_cabinet_by_id(cabinet_id)


@cabinet_router.get("/search/all", response_model=list[ShowCabinet], status_code=200)
async def get_all_cabinets(
    cabinet_service: Annotated[CabinetService, Depends(CabinetService)],
    pagination: Annotated[Pagination, Depends()],
):
    return await cabinet_service._get_all_cabinets(pagination)


@cabinet_router.get(
    "/search/by-building/{building_number}",
    response_model=list[ShowCabinet],
    status_code=200,
)
async def get_cabinets_by_building(
    building_number: int,
    cabinet_service: Annotated[CabinetService, Depends(CabinetService)],
    pagination: Annotated[Pagination, Depends()],
):
    return await cabinet_service._get_cabinets_by_building(building_number, pagination)


@cabinet_router.delete("/delete/{cabinet_id}", response_model=bool, status_code=200)
async def delete_cabinet(
    cabinet_id: int, cabinet_service: Annotated[CabinetService, Depends(CabinetService)]
):
    return await cabinet_service._delete_cabinet(cabinet_id)


@cabinet_router.put("/update/{cabinet_id}", response_model=ShowCabinet, status_code=200)
async def update_cabinet(
    cabinet_id: int,
    body: UpdateCabinet,
    cabinet_service: Annotated[CabinetService, Depends(CabinetService)],
):
    return await cabinet_service._update_cabinet(cabinet_id, body)
