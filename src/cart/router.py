from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy import select, join
from sqlalchemy.ext.asyncio import AsyncSession

from src.cart.schemas import CartItem
from src.database import get_async_session
from src.products.models import product
from src.cart.models import cart


router = APIRouter(
    prefix="/cart",
    tags=["Cart"]
)


@router.post("/add")
async def add_to_cart(item: CartItem, session: AsyncSession = Depends(get_async_session)):
    query = select(product).filter(product.c.id == item.product_id)
    result = await session.execute(query)
    product_exists = result.scalar()
    if not product_exists:
        raise HTTPException(status_code=404, detail="Продукт не найден")

    cart_item = CartItem(product_id=item.product_id, quantity=item.quantity)
    # Ваша логика для добавления товара в корзину

    return {"message": "Товар успешно добавлен в корзину", "cart_item": cart_item}


@router.get("/")
async def view_cart(session: AsyncSession = Depends(get_async_session)):
    # Получите информацию о корзине из базы данных
    query = select(cart.c.product_id, cart.c.quantity)
    result = await session.execute(query)
    items = result.fetchall()

    # Верните информацию о корзине
    return {"message": "Страница Корзина", "cart_items": items}
