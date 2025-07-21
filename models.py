from sqlalchemy import Integer , Column, Boolean , ForeignKey , String
from database import Base

class Questions(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    question = Column(String , index=True)
 
class Choices(Base):
    __tablename__ = 'choices'
    id = Column(Integer, primary_key=True)
    choice_text = Column(String , index= True)
    is_correct = Column(Boolean, default=False)
    question_id = Column(Integer , ForeignKey("question.id"))