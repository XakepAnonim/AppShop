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

    cart_items = relationship("CartItem", back_populates="product")
