from app.core.base_repository import BaseRepository
from app.db.models.specialty import Specialty


class SpecialtyRepository(BaseRepository):
    model = Specialty
