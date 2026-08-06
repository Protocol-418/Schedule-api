from app.core.base_repository import BaseRepository
from app.db.models.certification import Certification


class CertificationRepository(BaseRepository):
    model = Certification
