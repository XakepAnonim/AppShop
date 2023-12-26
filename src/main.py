from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from src.user.router import router as router_user
from src.products.router import router as router_product
from src.cart.router import router as router_cart
from src.order.router import router as router_order
from src.pages.router import router as router_pages

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


# @app.get("/", response_class=HTMLResponse)
# async def index(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})

app.include_router(router_user)
app.include_router(router_product)
app.include_router(router_cart)
app.include_router(router_order)
app.include_router(router_pages)
