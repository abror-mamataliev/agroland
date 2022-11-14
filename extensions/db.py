from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db: SQLAlchemy = SQLAlchemy()


def register_db(app: Flask) -> None:
    db.init_app(app)
    with app.app_context():
        db.create_all()
