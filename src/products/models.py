from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData, Date, Boolean
from sqlalchemy.orm import relationship

from src.database import Base

metadata = MetaData()

product = Table(
    "product",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=True),
    Column("type", String, nullable=True),
    Column("variety", String, nullable=True),
    Column("manufacturer", String, nullable=True),
    Column("description", String, nullable=True),
    Column("price", String, nullable=True),
    Column("stock", Integer, nullable=True),
    Column("date", TIMESTAMP),
    Column("photo", String, nullable=True),
)


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)
    variety = Column(String)
    manufacturer = Column(String)
    description = Column(String)
    price = Column(String)
    stock = Column(Integer)
    date = Column(Date)
    photo = Column(String, nullable=True, default='media/products/img123.png')

    cart_items = relationship("CartItem", back_populates="product")
    orders = relationship("Order", back_populates="product")
