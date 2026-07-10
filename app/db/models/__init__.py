"""В этом файле собираем все модели БД для алембика"""

from app.db.models.base import Base
from app.db.models.user import User

# Атрибут __all__ указывает какие модели должны экспортироваться
# при экспорте всей папки: from models import *
__all__ = ("Base", "User")