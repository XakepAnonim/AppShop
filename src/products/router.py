import time

from fastapi import APIRouter, Depends, HTTPException
from fastapi_cache.decorator import cache
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.products.models import product
from src.products.schemas import ProductCreate

router = APIRouter(
    prefix="/products",
    tags=["Product"]
)


@router.get('/long_products')
@cache(expire=30)
def get_long_op():
    time.sleep(2)
    return "Вычисления"


@router.get("")
async def get_specific_products(product_type: str, session: AsyncSession = Depends(get_async_session)):
    """
    Получает список продуктов определенного типа.

    Args:
        product_type (str): Тип продукта.
        session (AsyncSession, optional): Асинхронная сессия для работы с базой данных. Defaults to Depends(get_async_session).

    Returns:
        dict: Словарь с результатом запроса.
    """
    try:
        query = select(product).where(product.c.type == product_type)
        result = await session.execute(query)
        return {
            "status": "success",
            "data": result.all(),
            "details": None
        }
    except Exception:
        # Передать ошибку разработчикам
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })


@router.post("")
async def add_specific_products(new_product: ProductCreate, session: AsyncSession = Depends(get_async_session)):
    """
    Добавляет новый продукт.

    Args:
        new_product (ProductCreate): Данные нового продукта.
        session (AsyncSession, optional): Асинхронная сессия для работы с базой данных. Defaults to Depends(get_async_session).

    Returns:
        dict: Словарь с результатом операции.
    """
    stmt = insert(product).values(**new_product.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
