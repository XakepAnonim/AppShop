from sqlalchemy import Table, Column, Integer, String, ForeignKey, Enum, MetaData
from sqlalchemy.orm import relationship
from src.database import Base

metadata = MetaData()


order = Table(
    "order",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("user_id", Integer, ForeignKey("user.id")),
    Column("product_id", Integer, ForeignKey("product.id")),
    Column("status", Enum("In Progress", "Shipped", "Delivered",
                          name='order_status_enum'), default="In Progress")
)


class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    product_id = Column(Integer, ForeignKey("product.id"))
    status = Column(Enum("In Progress", "Shipped", "Delivered", name="order_status_enum"), default="In Progress")

    product = relationship("Product", back_populates="orders")
    user = relationship("User", back_populates="orders")

