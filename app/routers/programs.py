# app/routers/programs.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas import schemas
from app.crud import crud
from app.database import SessionLocal

router = APIRouter(prefix="/programs", tags=["Programs"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Program)
def create_program(program: schemas.ProgramCreate, db: Session = Depends(get_db)):
    return crud.create_program(db, program)

@router.get("/", response_model=List[schemas.Program])
def list_programs(db: Session = Depends(get_db)):
    return crud.get_programs(db)
