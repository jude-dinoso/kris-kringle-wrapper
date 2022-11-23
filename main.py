from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.database import Database
from src.models.login import Login
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "https://sjreunion.vercel.app/kris-kringle",
    "https://sjreunion.vercel.app/dashboard/default",
    "https://sjreunion.vercel.app",
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
async def login(first_name: str, password: str):
    login_params = Login(first_name=first_name, password=password)
    if database.login(login_params):
        return database.get_user_data(first_name)
    raise HTTPException(status_code=404, detail="Invalid User/Password")


@app.get("/participants/")
async def get_participants() -> list[str]:
    return database.get_participants()


@app.post("/wishlist/")
async def update_wishlist(
    first_name: str, wish_list: str, wish_list_2: str, wish_list_3: str
) -> str:
    update_query = f"UPDATE users SET wish_list = '{wish_list}', wish_list_2 = '{wish_list_2}', wish_list_3 = '{wish_list_3}' WHERE first_name = '{first_name}'"
    if database.execute_sql(update_query):
        return database.get_user_data(first_name)
    raise HTTPException(status_code=500, detail="Connection Error")


@app.post("/description/")
async def update_description(first_name: str, description: str) -> str:
    update_query = f"UPDATE users SET description = '{description}' WHERE first_name = '{first_name}'"
    if database.execute_sql(update_query):
        return database.get_user_data(first_name)
    raise HTTPException(status_code=500, detail="Connection Error")
