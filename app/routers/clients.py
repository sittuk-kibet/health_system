# app/routers/clients.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from app.schemas import schemas
from app.crud import crud
from app.database import SessionLocal

router = APIRouter(prefix="/clients", tags=["Clients"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Client)
def create_client(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    return crud.create_client(db, client)

@router.get("/{client_id}", response_model=schemas.Client)
def get_client(client_id: int, db: Session = Depends(get_db)):
    db_client = crud.get_client(db, client_id)
    if not db_client:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_client

@router.get("/", response_model=List[schemas.Client])
def search_clients(name: Optional[str] = "", db: Session = Depends(get_db)):
    return crud.search_clients_by_name(db, name)

@router.post("/{client_id}/enroll", response_model=schemas.Client)
def enroll_client(client_id: int, program_ids: List[int], db: Session = Depends(get_db)):
    client = crud.enroll_client(db, client_id, program_ids)
    if client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return client
