from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from pydantic import BaseModel
from datetime import date
from app.db import SessionLocal
import app.crud as crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/inventory/")
def read_inventory(db: Session = Depends(get_db)):
    return crud.get_all_items(db)

@router.get("/inventory/low-stock")
def low_stock(db: Session = Depends(get_db)):
    return crud.get_low_stock(db)

@router.get("/inventory/restocks")
def restocks(db: Session = Depends(get_db)):
    return crud.get_upcoming_restocks(db)

class InventoryCreate(BaseModel):
    product_name: str
    category: str
    quantity: int
    restock_date: date

@router.post("/inventory/")
def create_inventory(item: InventoryCreate, db: Session = Depends(get_db)):
    return crud.create_item(db, item.dict())