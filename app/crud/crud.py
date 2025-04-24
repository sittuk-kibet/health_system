# app/crud/crud.py

from sqlalchemy.orm import Session
from app.models import models
from app.schemas import schemas


# Create a new client

def create_client(db: Session, client: schemas.ClientCreate):
    db_client = models.Client(name=client.name, age=client.age)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client


# Create a new health program

def create_program(db: Session, program: schemas.ProgramCreate):
    db_program = models.Program(name=program.name)
    db.add(db_program)
    db.commit()
    db.refresh(db_program)
    return db_program


# Get a client by ID

def get_client(db: Session, client_id: int):
    return db.query(models.Client).filter(models.Client.id == client_id).first()

# Search for clients by name
def search_clients_by_name(db: Session, name: str):
    return db.query(models.Client).filter(models.Client.name.contains(name)).all()

# Get all health programs

def get_programs(db: Session):
    return db.query(models.Program).all()


# Enroll a client into one or more health programs

def enroll_client(db: Session, client_id: int, program_ids: list[int]):
    client = db.query(models.Client).get(client_id)
    if not client:
        return None

    # Add each program to the client's list (if not already enrolled)
    for pid in program_ids:
        program = db.query(models.Program).get(pid)
        if program and program not in client.programs:
            client.programs.append(program)

    db.commit()
    db.refresh(client)
    return client
