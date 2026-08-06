from app.core.base_repository import BaseRepository
from app.db.models.semester import Semester


class SemesterRepository(BaseRepository):
    model = Semester
