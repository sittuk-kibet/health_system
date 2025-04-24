# app/main.py

from fastapi import FastAPI
from app.database import engine
from app.models import models
from app.routers import clients, programs

# Create all tables
models.Base.metadata.create_all(bind=engine)

# Initialize app
app = FastAPI(title="Health Info System")

# Register routers
app.include_router(clients.router)
app.include_router(programs.router)

# Define a root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the Health Info System API!"}