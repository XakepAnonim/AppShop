from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from src.order.schemas import OrderCreate
from src.database import get_async_session
from src.order.models import Order, order

from src.auth.base_config import current_user as get_current_user
from src.user.models import User

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.get("")
async def get_all_products(session: AsyncSession = Depends(get_async_session)):
    query = select(order)
    result = await session.execute(query)
    orders = [row._asdict() for row in result.all()]
    return {"Заказы": orders}


@router.post("/")
async def create_order(order: OrderCreate, session: AsyncSession = Depends(get_async_session)):
    new_order = Order(id=order.id, user_id=order.user_id, product_id=order.product_id)
    session.add(new_order)
    await session.commit()
    await session.refresh(new_order)

    return {"Сообщение": "Заказ успешно создан", "Заказ": new_order}


@router.put("/{order_id}/status")
async def update_order_status(order_id: int, status: str, session: AsyncSession = Depends(get_async_session),
                              current_user: User = Depends(get_current_user)):
    if not current_user.is_superuser:
        raise HTTPException(status_code=403, detail="Пользователь не имеет права выполнять это действие")

    query = update(order).where(order.c.id == order_id).values(status=status)
    await session.execute(query)
    await session.commit()

    return {"Сообщение": "Статус заказа успешно обновлен"}
