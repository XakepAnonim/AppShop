from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.cart.schemas import CartItemCreate
from src.database import get_async_session
from src.products.models import product
from src.cart.models import cart, CartItem


router = APIRouter(
    prefix="/cart",
    tags=["Cart"]
)


@router.get("/")
async def view_cart(session: AsyncSession = Depends(get_async_session)):
    query = select(cart.c.product_id, cart.c.quantity)
    result = await session.execute(query)
    items = [row._asdict() for row in result.all()]

    # Верните информацию о корзине
    return {"Сообщение": "Корзина", "Товар": items}


@router.post("/add")
async def add_to_cart(item: CartItemCreate, session: AsyncSession = Depends(get_async_session)):
    query = select(product).filter(product.c.id == item.product_id)
    result = await session.execute(query)
    product_exists = result.scalar()
    if not product_exists:
        raise HTTPException(status_code=404, detail="Продукт не найден")

    cart_query = select(cart).filter(cart.c.id == item.id)
    cart_obj = await session.execute(cart_query)

    new_cart = CartItem(product_id=item.product_id, quantity=item.quantity)
    session.add(new_cart)

    await session.commit()
    return {"Сообщение": "Товар успешно добавлен в корзину"}
