from app.core.base_repository import BaseRepository
from app.db.models.class_session_type import ClassSessionType


class ClassSessionTypeRepository(BaseRepository):
    model = ClassSessionType
