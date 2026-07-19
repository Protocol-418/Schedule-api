from app.core.base_repository import BaseRepository
from app.db.models.teachers_category import TeachersCategory


class TeacherCategoryRepository(BaseRepository):
    model = TeachersCategory