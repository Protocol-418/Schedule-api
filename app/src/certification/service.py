from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.dependies import get_db
from app.core.exceptions.exceptions import ConflictException, NotFoundException
from app.db.models.certification import Certification
from app.src.certification.repository import CertificationRepository
from app.src.certification.schemas import CreateCertification, UpdateCertification


class CertificationService:
    def __init__(self, session: Annotated[AsyncSession, Depends(get_db)]):
        self.session = session
        self.certification_repo = CertificationRepository(self.session)

    async def _get_certification_by_subject_id(self, subject_id: int) -> Certification:
        """Получение формы аттестации по ID дисциплины"""
        certification = await self.certification_repo.get_entity_by_filter(subject_id=subject_id)
        if not certification:
            raise NotFoundException(
                service="Certification",
                message="Форма аттестации для данной дисциплины не найдена",
            )
        return certification

    async def _get_all_certifications(self) -> list[Certification]:
        """Получение всех форм аттестации"""
        certifications = await self.certification_repo.get_all_entities()
        return certifications

    async def _create_certification(self, certification_data: CreateCertification) -> Certification:
        """Создание новой формы аттестации"""
        is_exist = await self.certification_repo.get_entity_by_filter(subject_id=certification_data.subject_id)
        if is_exist:
            raise ConflictException(
                message="Форма аттестации для данной дисциплины уже существует",
                service="Certification",
            )

        certification = Certification(
            subject_id=certification_data.subject_id,
            credit=certification_data.credit,
            differentiated_credit=certification_data.differentiated_credit,
            course_project=certification_data.course_project,
            course_work=certification_data.course_work,
            control_work=certification_data.control_work,
            other_form=certification_data.other_form,
        )

        new_certification = await self.certification_repo.create_entity(certification)
        return new_certification

    async def _delete_certification(self, subject_id: int) -> bool:
        """Удаление формы аттестации"""
        certification = await self._get_certification_by_subject_id(subject_id)
        delete_result = await self.certification_repo.delete_entity(certification)
        return delete_result

    async def _update_certification(
        self, subject_id: int, certification_data: UpdateCertification
    ) -> Certification:
        """Обновление формы аттестации"""
        certification = await self._get_certification_by_subject_id(subject_id)

        updated_data = certification_data.model_dump(exclude_unset=True)
        for field, value in updated_data.items():
            setattr(certification, field, value)

        updated_certification = await self.certification_repo.update_entity(certification)
        return updated_certification
