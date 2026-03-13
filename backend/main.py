from fastapi import FastAPI
from database.db import engine, Base, UPLOAD_DIR
from router.api import api
from fastapi.middleware.cors import CORSMiddleware
import os
app = FastAPI()
origin = [
    "http://localhost:8501",
    "http://127.0.0.1:8501"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
Base.metadata.create_all(bind=engine)
os.makedirs(UPLOAD_DIR,exist_ok=True)

app.include_router(api)
