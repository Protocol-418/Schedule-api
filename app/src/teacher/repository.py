from app.core.base_repository import BaseRepository
from app.db.models.teacher import Teacher


class TeacherRepository(BaseRepository):
    model = Teacher