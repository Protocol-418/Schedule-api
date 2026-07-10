from app.core.base_repository import BaseRepository
from app.db.models.user import User


class UserRepository(BaseRepository):
    model = User