from dataclasses import dataclass
from datetime import datetime


@dataclass(init=False)
class User:

    id: int
    first_name: str
    last_name: str
    username: str
    password: str
    email: str
    created_at: datetime
    last_login: datetime

    def save(self):
        pass
