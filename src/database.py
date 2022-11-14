from typing import List

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI
from pydantic import BaseModel
from .models.login import Login

# SQLAlchemy specific code, as with any other app
_DATABASE_URL = "postgresql://boldzzuhsgcpzh:b37a76311f137c92e1799a5eed360bb17d9762844d4b5c1054b41b88aaa0b192@ec2-3-219-135-162.compute-1.amazonaws.com:5432/da9hlho92lgimc"

class Database:

    def __init__(self) -> None:
        self.engine = create_engine(_DATABASE_URL)

    def create_session(self) -> None:
        self.session = sessionmaker(bind = self.engine)

    def login(self, login_params: Login) -> bool:
        login_query = f"SELECT * FROM login WHERE first_name = '{login_params.first_name}' AND password = '{login_params.password}'"
        data = self.engine.execute(login_query)
        if data:
            return True
        return False

    
