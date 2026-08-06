from app.core.base_repository import BaseRepository
from app.db.models.building import Building


class BuildingRepository(BaseRepository):
    model = Building
