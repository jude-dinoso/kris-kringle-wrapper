from pydantic import BaseModel
from datetime import datetime


class User(BaseModel):
    first_name: str
    group_id: int
    wish_list: str | None = None
    recipient: str | None = None
    recipient_update_time: datetime | None = None
    description: str | None = None
    description_update_time: datetime | None = None
    secret_santa: str | None = None
    secret_santa_update_time: datetime | None = None
