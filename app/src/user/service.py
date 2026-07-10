from app.core.dependies import get_db
from app.core.exceptions.exceptions import NotFoundException, ConflictException
from app.src.user.repository import UserRepository
from app.src.user.schemas import CreateUser, UpdateUser
from app.core.security.password import get_password_hash
from app.db.models.user import User

from typing import Annotated
from uuid import UUID

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession


class UserService:
    def __init__(self, session: Annotated[AsyncSession, Depends(get_db)]):
        self.session = session
        self.user_repo = UserRepository(self.session)

    async def _get_user_by_uuid(self, uuid: UUID) -> User:
        """Получение пользователя по uuid"""
        user = await self.user_repo.get_entity_by_filter(uuid=uuid)
        if not user:
            raise NotFoundException(service="User", message="Пользователь с таким uuid не найден")
        return user
    
    async def _get_user_by_email(self, email: str) -> User:
        """Получение пользователя по email"""
        user = await self.user_repo.get_entity_by_filter(email=email)
        if not user:
            raise NotFoundException(service="User", message="Пользователь с таким email не найден")
        return user

    async def _get_users_by_role(self, role: str) -> list[User]:
        """Получение всех пользователей по роли"""
        users = await self.user_repo.get_entities_by_filter(role=role)
        return users

    async def _get_all_users(self) -> list[User]:
        """Получение всех пользователей"""
        users = await self.user_repo.get_all_entities()
        return users

    async def _create_user(self, user_data: CreateUser) -> User:
        """Создание нового пользователя"""
        # Если пользователь с таким email существует
        is_email_exist = await self.user_repo.get_entity_by_filter(email=user_data.email)
        if is_email_exist:
            raise ConflictException(message="Пользователь с таким email уже зарегистрирован", service="User")

        user = User(
            username=user_data.username,
            email=user_data.email,
            role=user_data.role,
            hashed_password=get_password_hash(user_data.password)
        )

        new_user = await self.user_repo.create_entity(user)
        return new_user

    async def _delete_user(self, uuid: UUID) -> bool:
        """Удаление пользователя"""
        user = await self._get_user_by_uuid(uuid)
        delete_result = await self.user_repo.delete_entity(user)
        return delete_result

    async def _update_user(self, uuid: UUID, user_data: UpdateUser) -> User:
        """Обновление пользователя"""
        user = await self._get_user_by_uuid(uuid)

        # Преобразуем в dict, исключая поля равные None
        updated_user_data = user_data.model_dump(exclude_unset=True)
        for field, value in updated_user_data.items():
            # Т.к. поля orm модели это атрибуты класса, то выставляем им новые значения через setattr
            setattr(user, field, value)

        updated_user = await self.user_repo.update_entity(user)
        return updated_user
        

        

        


        
        

            
