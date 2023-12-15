from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from src.user.router import router as router_user
from src.products.router import router as router_product
from src.cart.router import router as router_cart


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

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


# @app.get("/auth")
# async def index(request: Request):
#     data = fastapi_users.get_register_router(UserRead, UserCreate)
#     return templates.TemplateResponse("registration/login.html", {"request": request, "data": data})

app.include_router(router_user)
app.include_router(router_product)
app.include_router(router_cart)
