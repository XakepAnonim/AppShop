from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.products.schemas import ProductCreate, ProductUpdate
from src.database import get_async_session
from src.products.models import Product, product

from src.user.models import User
from src.auth.base_config import current_user as get_current_user

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


# Получение товаров
@router.get("/")
async def get_all_products(product_type: str, session: AsyncSession = Depends(get_async_session)):
    query = select(product).where(product.c.type == product_type)
    result = await session.execute(query)
    products = [row._asdict() for row in result.all()]
    return {
        "status": "success",
        "data": products,
        "details": None
    }


@router.get("/{product_id}")
async def get_product(product_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(product).filter(product.c.id == product_id)
    result = await session.execute(query)
    one_product = result.first()
    if not one_product:
        raise HTTPException(status_code=404, detail="Продукт не найден")
    return one_product


# Добавление, изменение, удаление товара
@router.post("/")
async def add_product(product: ProductCreate, session: AsyncSession = Depends(get_async_session),
                      current_user: User = Depends(get_current_user)):
    if not current_user.is_superuser:
        raise HTTPException(status_code=403, detail="User is not authorized to perform this action")
    new_product = Product(
        name=product.name,
        type=product.type,
        variety=product.variety,
        manufacturer=product.manufacturer,
        description=product.description,
        price=product.price,
        stock=product.stock,
        date=product.date
    )
    session.add(new_product)
    await session.commit()
    await session.refresh(new_product)
    return new_product


@router.put("/{product_id}")
async def update_product(product_id: int, updated_product: ProductUpdate,
                         session: AsyncSession = Depends(get_async_session)):
    query = select(product).filter(product.c.id == product_id)
    result = await session.execute(query)
    existing_product = result.first()
    if not existing_product:
        raise HTTPException(status_code=404, detail="Продукт не найден")

    # Создаем новый объект Product с обновленными атрибутами
    updated_product_data = updated_product.dict()
    updated_product_obj = Product(**updated_product_data)

    # Обновляем запись в базе данных
    query = (
        update(product)
        .where(product.c.id == product_id)
        .values(**updated_product_data)
    )
    await session.execute(query)
    await session.commit()

    # Возвращаем обновленный продукт
    return updated_product_obj


@router.delete("/{product_id}")
async def delete_product(product_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Product).filter(Product.id == product_id)
    result = await session.execute(query)
    del_product = result.scalar_one_or_none()
    if not del_product:
        raise HTTPException(status_code=404, detail="Продукт не найден")
    if not del_product.stock == 0:
        raise HTTPException(status_code=400, detail="Товар недоступен")
    await session.delete(del_product)
    await session.commit()
    return {"message": "Product deleted successfully"}


# Уведомление о товаре
@router.post("/{product_id}/notify")
async def notify_product_availability(product_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(product).filter(product.c.id == product_id)
    result = await session.execute(query)
    nof_product = result.first()
    if not nof_product:
        raise HTTPException(status_code=404, detail="Товар не найден")
    if nof_product.stock < 0:
        raise HTTPException(status_code=400, detail="Товар недоступен")
    if nof_product.stock == 0:
        raise HTTPException(status_code=400, detail="Товар недоступен")
    # Здесь реализовать логику отправки уведомления
    return {"message": "Notification set"}
