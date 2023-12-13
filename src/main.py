from fastapi import FastAPI, Request
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from redis import asyncio as aioredis
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

from src.auth.base_config import auth_backend, fastapi_users
from src.auth.schemas import UserRead, UserCreate

from src.products.router import router as router_product
# from src.auth.router import router as router_auth


app = FastAPI(
    title="AppShop"
)

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)


@app.get("/auth")
async def index(request: Request):
    data = fastapi_users.get_register_router(UserRead, UserCreate)
    return templates.TemplateResponse("registration/login.html", {"request": request, "data": data})

app.include_router(router_product)


@app.on_event("startup")
async def startup_event():
    redis = aioredis.from_url("redis://localhost", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
