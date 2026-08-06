from app.core.base_repository import BaseRepository
from app.db.models.cabinet import Cabinet


class CabinetRepository(BaseRepository):
    model = Cabinet
