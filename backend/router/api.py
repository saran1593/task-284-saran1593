from fastapi import APIRouter, Depends, UploadFile, File
from models.schema import Login, CreateStudent, Student, Questions
from services.orm_service import create_student, get_student_by_id, get_students, login, upload_file, downlod_file
api = APIRouter()
from database.deps import get_db
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from services.rag import rag_pipeline
auth = OAuth2PasswordBearer(tokenUrl="login")

@api.get("/get-students")
def get_student(token: str= Depends(auth),db:Session=Depends(get_db)):
    return get_students(db)

@api.post("/login")
def login_user(user: Login, db:Session=Depends(get_db)):
    return login(db, user.email, user.password)

@api.post("/create-student")
def create_students(student: CreateStudent, db:Session=Depends(get_db)):
    return create_student(db,student.name, student.email,student.password)

@api.post("/get-student-by-id")
def get_studentbyid(student_id: Student):
    return get_student_by_id(student_id.id)

@api.post("/upload-file")
def upload_file_data(token: str= Depends(auth),file: UploadFile = File(...)):
    return upload_file(file)


@api.get("/download/{file_name}")
def download_file_data(file_name: str, token: str= Depends(auth)):
    return downlod_file(file_name)

@api.post("/rag")
def rag_endpoint(question: Questions, db:Session=Depends(get_db)):
    return rag_pipeline(db, question.question)