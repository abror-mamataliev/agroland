from datetime import datetime

from extensions import db


class BaseModel(db.Model):  # type: ignore

    __abstract__: bool = True

    __tablename__: str

    id = db.Column(db.Integer, primary_key=True)

    def save(self):
        db.session.add(self)
        db.session.commit()


class TimestampMixin:

    created_at = db.Column(db.DateTime(), default=datetime.now)
    updated_at = db.Column(db.DateTime(), onupdate=datetime.now)
