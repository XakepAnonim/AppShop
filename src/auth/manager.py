from typing import Optional

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin, exceptions, models, schemas

from src.user.models import User
from src.auth.utils import get_user_db

from src.config import SECRET_AUTH


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    """
    Класс UserManager предоставляет методы для управления пользователями.

    Args:
        IntegerIDMixin: Миксин для работы с пользователями, у которых идентификаторы являются целыми числами.
        BaseUserManager: Базовый класс для управления пользователями.

    Attributes:
        reset_password_token_secret (str): Секретный ключ для сброса пароля пользователя.
        verification_token_secret (str): Секретный ключ для подтверждения пользователя.
    """
    reset_password_token_secret = SECRET_AUTH
    verification_token_secret = SECRET_AUTH

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        """
        Выполняется после успешной регистрации пользователя.

        Args:
            user (User): Зарегистрированный пользователь.
            request (Optional[Request], optional): Объект запроса. Defaults to None.
        """
        print(f"Пользователь {user.id} зарегистрирован.")

    async def create(
        self,
        user_create: schemas.UC,
        safe: bool = False,
        request: Optional[Request] = None,
    ) -> models.UP:
        """
        Создает нового пользователя.

        Args:
            user_create (schemas.UC): Схема данных для создания пользователя.
            safe (bool, optional): Флаг безопасного режима создания пользователя. Defaults to False.
            request (Optional[Request], optional): Объект запроса. Defaults to None.

        Returns:
            models.UP: Созданный пользователь.
        """
        await self.validate_password(user_create.password, user_create)

        existing_user = await self.user_db.get_by_email(user_create.email)
        if existing_user is not None:
            raise exceptions.UserAlreadyExists()

        user_dict = (
            user_create.create_update_dict()
            if safe
            else user_create.create_update_dict_superuser()
        )
        password = user_dict.pop("password")
        user_dict["hashed_password"] = self.password_helper.hash(password)

        created_user = await self.user_db.create(user_dict)

        await self.on_after_register(created_user, request)

        return created_user


async def get_user_manager(user_db=Depends(get_user_db)):
    """
    Возвращает экземпляр класса UserManager для управления пользователями.

    Args:
        user_db (Depends): Зависимость для получения базы данных пользователей.

    Yields:
        UserManager: Экземпляр класса UserManager.
    """
    yield UserManager(user_db)
