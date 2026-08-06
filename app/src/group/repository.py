from app.core.base_repository import BaseRepository
from app.db.models.group import Group


class GroupRepository(BaseRepository):
    model = Group
