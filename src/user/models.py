from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, Boolean, MetaData
from sqlalchemy.orm import relationship

from src.database import Base

metadata = MetaData()

user = Table(  # Императивный метов запроса SqlAlchemy
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("hashed_password", String, nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
)


class User(SQLAlchemyBaseUserTable[int], Base):
    """
    Декларативный метод запроса SqlAlchemy
    #
    Класс User представляет модель пользователя в базе данных.

    Args:
        SQLAlchemyBaseUserTable: Базовая таблица пользователей для SQLAlchemy.
        Base: Базовый класс модели базы данных.

    Attributes:
        Column - Колонка
        id (Column): Идентификатора пользователя.
        email (Column): Электронная почта пользователя.
        username (Column): Имя пользователя.
        registered_at (Column): Даты и время регистрации пользователя.
        hashed_password (Column): Хешированный пароль пользователя.
        is_active (Column): Флаг активности пользователя.
        is_superuser (Column): Флаг суперпользователя.
        is_verified (Column): Флаг подтверждения пользователя.
    """
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    hashed_password: str = Column(String(length=1024), nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)

    orders = relationship("Order", back_populates="user")
