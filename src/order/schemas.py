from pydantic import BaseModel


class OrderCreate(BaseModel):
    id: int
    user_id: int
    product_id: int
