from typing import List

from fastapi import FastAPI
from pydantic import BaseModel
from src.database import Database
from src.models.login import Login
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "https://sjreunion.vercel.app/kris-kringle",
    "https://sjreunion.vercel.app/dashboard/default",
    "https://sjreunion.vercel.app/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
database = Database()

@app.post("/login/")
async def login(first_name: str, password: str) -> bool:
    login_params = Login(first_name=first_name, password=password)
    if database.login(login_params):
        return database.get_user_data(first_name)

@app.get("/participants/")
async def get_participants() -> list[str]:
    return database.get_participants()



