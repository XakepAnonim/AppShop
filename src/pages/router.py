from fastapi import Request, Depends, APIRouter
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from src.order.models import order
from src.cart.models import cart
from src.database import get_async_session
from src.products.models import product
from src.user.models import user

router = APIRouter(
    prefix="",
    tags=["AppShop"]
)

templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def get_all_products(request: Request, session: AsyncSession = Depends(get_async_session)):
    query = select(product)
    result = await session.execute(query)
    products = [row._asdict() for row in result.all()]
    return templates.TemplateResponse("index.html", {
        "request": request, "products": products})


# @router.get("/{product_id}", response_class=HTMLResponse)
# async def get_product(request: Request, product_id: int, session: AsyncSession = Depends(get_async_session)):
#     query = select(product).filter(product.c.id == product_id)
#     result = await session.execute(query)
#     products = [row._asdict() for row in result.all()]
#     return templates.TemplateResponse("product.html", {
#         "request": request, "products": products})


@router.get('/cart', response_class=HTMLResponse)
async def get_cart(request: Request, session: AsyncSession = Depends(get_async_session)):
    query = select(cart)
    result = await session.execute(query)
    carts = [row._asdict() for row in result.all()]

    query1 = select(product)
    result1 = await session.execute(query1)
    products = [row._asdict() for row in result1.all()]

    query2 = select(user)
    result2 = await session.execute(query2)
    users = [row._asdict() for row in result2.all()]
    return templates.TemplateResponse("index.html", {
        "request": request, "carts": carts, "products": products, "users": users
    })


# @router.get('/orders', response_class=HTMLResponse)
# async def get_orders(request: Request, session: AsyncSession = Depends(get_async_session)):
#     query = select(order)
#     result = await session.execute(query)
#     orders = [row._asdict() for row in result.all()]
#     return templates.TemplateResponse("orders.html", {
#         "request": request, "orders": orders
#     })


@router.get('/profile/{user_id}/{product_id}', response_class=HTMLResponse)
async def get_profile(request: Request, user_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(user).filter(user.c.id == user_id)
    result = await session.execute(query)
    users = [row._asdict() for row in result.all()]
    return templates.TemplateResponse("profile.html", {
        "request": request, "users": users
    })


@router.get('/buy', response_class=HTMLResponse)
async def buy(request: Request):
    return templates.TemplateResponse("buy.html", {"request": request})
