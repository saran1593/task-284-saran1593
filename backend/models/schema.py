from pydantic import BaseModel


class Login(BaseModel):
    email: str
    password: str

class CreateStudent(BaseModel):
    name: str
    email: str
    password: str

class Student(BaseModel):
    id: int
    
class Questions(BaseModel):
    question: str
