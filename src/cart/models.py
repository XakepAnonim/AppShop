from sqlalchemy import Table, MetaData, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from src.database import Base

metadata = MetaData()


cart = Table(
    "cart_item",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("user_id", Integer, ForeignKey("user.id")),
    Column("product_id", Integer, ForeignKey("product.id", ondelete='CASCADE')),
    Column("quantity", Integer)
)


class CartItem(Base):
    __tablename__ = "cart_item"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    product_id = Column(Integer, ForeignKey("product.id", ondelete='CASCADE'))
    quantity = Column(Integer)

    user = relationship("User", back_populates="cart_items")
    product = relationship("Product", back_populates="cart_items")
