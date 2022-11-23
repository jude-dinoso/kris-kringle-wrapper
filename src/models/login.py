from pydantic import BaseModel
from datetime import datetime


class Login(BaseModel):
    first_name: str
    password: str | None = None
    last_accessed_at: datetime | None = None
