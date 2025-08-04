from sqlalchemy.orm import Session
from app.models import InventoryItem
from datetime import date, timedelta

def get_all_items(db: Session):
    return db.query(InventoryItem).all()

def get_low_stock(db: Session):
    return db.query(InventoryItem).filter(InventoryItem.quantity < 10).all()

def get_upcoming_restocks(db: Session):
    today = date.today()
    next_week = today + timedelta(days=7)
    return db.query(InventoryItem).filter(InventoryItem.restock_date.between(today, next_week)).all()

def create_item(db: Session, item_data: dict):
    item = InventoryItem(**item_data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
