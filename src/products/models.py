from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData

metadata = MetaData()

product = Table(
    "product",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=True),
    Column("category", String, nullable=True),
    Column("variety", String, nullable=True),
    Column("manufacturer", String, nullable=True),
    Column("description", String, nullable=True),
    Column("price", String, nullable=True),
    Column("quantity", String),
    Column("date", TIMESTAMP),
)
