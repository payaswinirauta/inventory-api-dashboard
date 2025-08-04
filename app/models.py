from sqlalchemy import Column, Integer, String, Date
from app.db import Base

class InventoryItem(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, index=True)
    category = Column(String)
    quantity = Column(Integer)
    restock_date = Column(Date)
