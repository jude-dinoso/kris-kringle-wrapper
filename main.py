from typing import List

from fastapi import FastAPI
from pydantic import BaseModel
from src.database import Database
from src.models.login import Login

app = FastAPI()
database = Database()

@app.post("/login/")
async def login(first_name: str, password: str) -> bool:
    login_params = Login(first_name=first_name, password=password)
    return database.login(login_params)
    pass


