from typing import List

import databases
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI
from pydantic import BaseModel

# SQLAlchemy specific code, as with any other app
DATABASE_URL = "postgresql://boldzzuhsgcpzh:b37a76311f137c92e1799a5eed360bb17d9762844d4b5c1054b41b88aaa0b192@ec2-3-219-135-162.compute-1.amazonaws.com:5432/da9hlho92lgimc"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

login = sqlalchemy.Table(
    "login",
    metadata,
    sqlalchemy.Column("first_name", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("password", sqlalchemy.String),
    sqlalchemy.Column("last_accessed_at", sqlalchemy.TIMESTAMP),
)

user = sqlalchemy.Table(
    "user",
    metadata,
    sqlalchemy.Column("first_name", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("group_id", sqlalchemy.Integer),
    sqlalchemy.Column("wish_list", sqlalchemy.String),
    sqlalchemy.Column("recipient", sqlalchemy.String),
    sqlalchemy.Column("recipient_update_time", sqlalchemy.TIMESTAMP),
    sqlalchemy.Column("description", sqlalchemy.String),
    sqlalchemy.Column("description_update_time", sqlalchemy.TIMESTAMP),
    sqlalchemy.Column("secret_santa", sqlalchemy.String),
    sqlalchemy.Column("secret_santa_update_time", sqlalchemy.TIMESTAMP),
)

class Database:

    def __init__(self) -> None:
        self.engine = sqlalchemy.create_engine(DATABASE_URL)

    def create_session(self) -> None:
        self.session = sessionmaker(bind = self.engine)

