from sqlalchemy import Table, MetaData, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from src.database import Base

metadata = MetaData()


cart = Table(
    "cart_item",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("product_id", Integer, ForeignKey("product.id")),
    Column("quantity", Integer),
)


class CartItem(Base):
    __tablename__ = "cart_item"
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("product.id"))
    quantity = Column(Integer)

    product = relationship("Product", back_populates="cart_items")


