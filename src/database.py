from typing import List

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .models.login import Login
import os

# SQLAlchemy specific code, as with any other app
_DATABASE_URL = os.environ["DATABASE_URL"].replace("postgres", "postgresql")


class Database:
    def __init__(self) -> None:
        self.engine = create_engine(_DATABASE_URL, connect_args={"sslmode": "require"})

    def create_session(self) -> None:
        self.session = sessionmaker(bind=self.engine)

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
        raise HTTPException(status_code=500, detail="Connection Error")

    def get_user_data(self, first_name: str):
        select_query = "SELECT u1.secret_santa, u1.recipient, u1.wish_list, u1.wish_list_2, u1.wish_list_3," \
                       " u2.wish_list as r_wl, u2.wish_list_2 as r_wl2, u2.wish_list_3 as r_wl3, u1.description from users u1 JOIN users u2" \
                       " on u1.recipient = u2.first_name" \
                       f" WHERE u1.first_name = '{first_name}';"
        data = self.engine.execute(select_query)
        if data:
            return data.first()
        raise HTTPException(status_code=500, detail="Connection Error")

    def execute_sql(self, query: str) -> bool:
        data = self.engine.execute(query)
        if data:
            return True
        raise HTTPException(status_code=500, detail="Connection Error")
