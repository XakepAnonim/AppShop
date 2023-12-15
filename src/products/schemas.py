from datetime import datetime

from pydantic import BaseModel


class ProductCreate(BaseModel):
    id: int
    name: str
    type: str
    variety: str
    manufacturer: str
    description: str
    price: str
    stock: int
    date: datetime


class ProductUpdate(BaseModel):
    name: str
    type: str
    variety: str
    manufacturer: str
    description: str
    price: str
    stock: int
