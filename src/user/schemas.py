from typing import Optional

from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    """
    Класс UserRead представляет схему для чтения информации о пользователе.

    Args:
        schemas.BaseUser: Базовая схема для пользователя.

    Attributes:
        id (int): Идентификатор пользователя.
        email (str): Электронная почта пользователя.
        username (str): Имя пользователя.
        is_active (bool, optional): Флаг активности пользователя. Defaults to True.
        is_superuser (bool, optional): Флаг суперпользователя. Defaults to False.
        is_verified (bool, optional): Флаг подтверждения пользователя. Defaults to False.

    """
    id: int
    email: str
    username: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        from_attributes = True


class UserCreate(schemas.BaseUserCreate):
    """
    Класс UserCreate представляет схему для создания пользователя.

    Args:
        schemas.BaseUserCreate: Базовая схема для создания пользователя.

    Attributes:
        username (str): Имя пользователя.
        email (str): Электронная почта пользователя.
        password (str): Пароль пользователя.
        is_active (Optional[bool], optional): Флаг активности пользователя. Defaults to True.
        is_superuser (Optional[bool], optional): Флаг суперпользователя. Defaults to False.
        is_verified (Optional[bool], optional): Флаг подтверждения пользователя. Defaults to False.

    """
    username: str
    email: str
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
