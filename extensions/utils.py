from flask import Flask


def register_extensions(app: Flask) -> None:
    from .auth import register_auth
    from .db import register_db
    
    register_db(app)
    register_auth(app)
