from typing import Annotated

from fastapi import APIRouter, Depends

from app.src.building.schemas import CreateBuilding, ShowBuilding, UpdateBuilding
from app.src.building.service import BuildingService

building_router = APIRouter(prefix="/building", tags=["buildings"])


@building_router.post("/create", response_model=ShowBuilding, status_code=201)
async def create_building(
    body: CreateBuilding,
    building_service: Annotated[BuildingService, Depends(BuildingService)]
):
    return await building_service._create_building(body)


@building_router.get("/search/by-number/{number}", response_model=ShowBuilding, status_code=200)
async def get_building_by_number(
    number: int,
    building_service: Annotated[BuildingService, Depends(BuildingService)]
):
    return await building_service._get_building_by_number(number)


@building_router.get("/search/all", response_model=list[ShowBuilding], status_code=200)
async def get_all_buildings(
    building_service: Annotated[BuildingService, Depends(BuildingService)]
):
    return await building_service._get_all_buildings()


@building_router.delete("/delete/{number}", response_model=bool, status_code=200)
async def delete_building(
    number: int,
    building_service: Annotated[BuildingService, Depends(BuildingService)]
):
    return await building_service._delete_building(number)


@building_router.put("/update/{number}", response_model=ShowBuilding, status_code=200)
async def update_building(
    number: int,
    body: UpdateBuilding,
    building_service: Annotated[BuildingService, Depends(BuildingService)]
):
    return await building_service._update_building(number, body)
