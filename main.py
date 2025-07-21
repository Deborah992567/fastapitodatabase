from multiprocessing.resource_tracker import getfd
from fastapi import Fastapi , HTTPException, Depends
from pydantic import BaseModel
from typing import List , Annotated
import models
from database import engine , SessionLocal
from sqlalchemy.orm import Session
models.Base.metadata.create_all(bind=engine) 

app = Fastapi()

class ChoiceBase(BaseModel):
    choice_text: str
    is_correct : bool
    
class QuestionBase(BaseModel):
    question_text : str
    choices : List[ChoiceBase]
    
def get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()
            
db_dependency = Annotated[Session,Depends(get_db)]            