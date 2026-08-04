"""В этом файле собираем все модели БД для алембика"""

from app.db.models.base import Base
from app.db.models.building import Building
from app.db.models.cabinet import Cabinet
from app.db.models.certification import Certification
from app.db.models.chapter_in_plan import ChapterInPlan
from app.db.models.class_session import ClassSession
from app.db.models.class_session_type import ClassSessionType
from app.db.models.cycle_in_chapter import CycleInChapter
from app.db.models.group import Group
from app.db.models.module_in_cycle import ModuleInCycle
from app.db.models.payment_form import PaymentForm
from app.db.models.plan import Plan
from app.db.models.semester import Semester
from app.db.models.specialty import Specialty
from app.db.models.stream import Stream
from app.db.models.subject import Subject
from app.db.models.teacher import Teacher
from app.db.models.teacher_assignment import TeacherAssignment
from app.db.models.teachers_category import TeachersCategory
from app.db.models.user import User

__all__ = (
    "Base",
    "Building",
    "Cabinet",
    "Certification",
    "ChapterInPlan",
    "ClassSession",
    "ClassSessionType",
    "CycleInChapter",
    "Group",
    "ModuleInCycle",
    "PaymentForm",
    "Plan",
    "Semester",
    "Specialty",
    "Stream",
    "Subject",
    "Teacher",
    "TeacherAssignment",
    "TeachersCategory",
    "User",
)
