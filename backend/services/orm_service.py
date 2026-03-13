from passlib.hash import argon2
from sqlalchemy.orm import Session
from models.user import User
from auth.auth import create_access_token
from database.db import UPLOAD_DIR
from fastapi import UploadFile, File 
import os 
import shutil
from fastapi.responses import FileResponse
import mimetypes

def upload_file(File:UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR,File.filename) 
    with open(file_path,"wb") as f:
        shutil.copyfileobj(File.file,f)
    return {"message": "File uploaded successfully"}

def downlod_file(file_name:str):
    file_path = os.path.join(UPLOAD_DIR,file_name) 
    if not file_path:
        return {"message": "File not found"}
    mime_type, _ = mimetypes.guess_type(file_path)
    return FileResponse (path = file_path, filename = file_name, media_type =mime_type or "application/octet-stream")
def create_student(db: Session, name: str, email:str, password: str):
    hashpassword = argon2.hash(password)
    new_user = User(name =name, email=email, password=hashpassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created successfully"}

def get_students(db: Session):
    users = db.query(User).all()

    return [
        {
            "name": u.name,
            "email": u.email,
        }
        for u in users
    ]

def get_student_by_id(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return {"message": "User not found"}

    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
    }

def login(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    
    if user and argon2.verify(password, user.password):
        token = create_access_token(data={"sub":user.email,"user_id":user.id})
        return {"message": "Login successful","token":token,"name":user.name}
    return {"message": "Invalid email or password"}

