from app.core.base_repository import BaseRepository
from app.db.models.plan import Plan


class PlanRepository(BaseRepository):
    model = Plan
