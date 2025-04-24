# app/schemas/schemas.py

from typing import List
from pydantic import BaseModel

# Program Schemas
class ProgramBase(BaseModel):
    name: str

class ProgramCreate(ProgramBase):
    pass

class Program(ProgramBase):
    id: int
    class Config:
        orm_mode = True

# Client Schemas
class ClientBase(BaseModel):
    name: str
    age: int

class ClientCreate(ClientBase):
    pass

class Client(ClientBase):
    id: int
    programs: List[Program] = []
    class Config:
        orm_mode = True
