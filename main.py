from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List, Optional
from models import Task as TaskModel
from models import Base
Base.metadata.create_all(bind=engine)

app = FastAPI()

class TaskCreate(BaseModel):
    title: str
    description: Optional[str]=None
class Tasks(BaseModel):
    id: int
    title: str
    description: Optional[str]=None
    completed: bool
    class Config:
        orm_mode=True
def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/create/", response_model= Tasks,status_code=202)
def create_task(
    task_data: TaskCreate,
    db: Session= Depends(get_db)):
    new_task=TaskModel(
        title=task_data.title,
        description=task_data.description
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


