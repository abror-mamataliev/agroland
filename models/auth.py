from dataclasses import dataclass
from datetime import datetime
from flask_login import UserMixin

from extensions import db

from .base import (
    BaseModel,
    TimestampMixin
)


class User(BaseModel, UserMixin):

    __tablename__: str = "auth_user"

    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    password = db.Column(db.String(255))
    email = db.Column(db.String(255), nullable=False, unique=True)
    created_at = db.Column(db.DateTime(), nullable=False, default=datetime.now())
    last_login = db.Column(db.DateTime())

    profile = db.relationship("Profile", backref="user", uselist=False)

    def __repr__(self) -> str:
        return self.email
    
    def __str__(self) -> str:
        return self.email
    
    def set_password(self, password: str) -> None:
        from werkzeug.security import generate_password_hash

        self.password = generate_password_hash(password)
    
    def check_password(self, password: str) -> bool:
        from werkzeug.security import check_password_hash

        return check_password_hash(self.password, password)


@dataclass(init=False)
class Profile(BaseModel, TimestampMixin):

    __tablename__: str = "auth_profile"

    user: User
    user_id = db.Column(db.Integer, db.ForeignKey("auth_user.id", ondelete="CASCADE"), nullable=False)
    image = db.Column(db.String(255), default="profile/images/default.png")

    polygons = db.relationship("Polygon", backref="profile")

    def __repr__(self) -> str:
        return self.user.email

    def __str__(self) -> str:
        return self.user.email
