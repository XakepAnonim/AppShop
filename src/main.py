from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.user.router import router as router_user
from src.products.router import router as router_product
from src.cart.router import router as router_cart
from src.order.router import router as router_order

app = FastAPI(
    title="AppShop"
)

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router_user)
app.include_router(router_product)
app.include_router(router_cart)
app.include_router(router_order)
