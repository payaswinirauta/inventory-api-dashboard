from fastapi import FastAPI
from app import models
from app.db import engine
from app.routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Inventory Insights API",
    description="Backend API to manage and analyze inventory data.",
    version="1.0.0"
)

app.include_router(router)
