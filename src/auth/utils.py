from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from src.user.models import User
from src.database import get_async_session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    """
    Возвращает экземпляр класса SQLAlchemyUserDatabase для работы с базой данных пользователей.

    Args:
        session (AsyncSession, optional): Асинхронная сессия SQLAlchemy. Defaults to Depends(get_async_session).
    """
    yield SQLAlchemyUserDatabase(session, User)
