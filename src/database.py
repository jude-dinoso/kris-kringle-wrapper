from typing import List

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI
from pydantic import BaseModel
from .models.login import Login

# SQLAlchemy specific code, as with any other app
_DATABASE_URL = "postgresql://guiedycdcumjhn:ecdfa9e4e380c9f6e88ed8137e37ddf23dacd9a86fadd8b057256c2c58227fb2@ec2-52-0-222-226.compute-1.amazonaws.com:5432/d5jush1mk1fk0a"

class Database:

    def __init__(self) -> None:
        self.engine = create_engine(_DATABASE_URL)

    def create_session(self) -> None:
        self.session = sessionmaker(bind = self.engine)

    def login(self, login_params: Login) -> bool:
        login_query = f"SELECT * FROM login WHERE first_name = '{login_params.first_name}' AND password = '{login_params.password}'"
        data = self.engine.execute(login_query).all()
        if len(data) == 1:
            return True
        return False

    def get_participants(self):
        select_query = "SELECT first_name from users;"
        data = self.engine.execute(select_query)
        if data:
            return data.all()
        raise Exception("Connection Error")

    def get_user_data(self, first_name:str):
        select_query = f"SELECT secret_santa, recipient, wish_list from users WHERE first_name = '{first_name}';"
        data = self.engine.execute(select_query)
        if data:
            return data.first()
        raise Exception("Connection Error")