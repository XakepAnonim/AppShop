from typing import List

from pydantic import BaseModel


class CartItem(BaseModel):
    user_id: int
    product_id: int
    quantity: int


class Cart(BaseModel):
    items: List[CartItem]


class CartItemCreate(BaseModel):
    id: int
    user_id: int
    product_id: int
    quantity: int
