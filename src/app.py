from typing import List

from fastapi import FastAPI
from pydantic import BaseModel
from .database import Database
from .models.login import Login

app = FastAPI()
database = Database()

@app.post("/login/")
async def login(login_params: Login) -> bool:
    return database.login(login_params) 
    pass


