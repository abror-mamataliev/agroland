from flask import Flask

from models import *
from routes import *


def create_app(type: str = "dev") -> Flask:
    from os.path import dirname

    from extensions import register_extensions
    from modules import register_modules

    app: Flask = Flask(dirname(dirname(__file__)), instance_path=dirname(dirname(__file__)))
    app.config.from_object(f"config.{type.capitalize()}Config")
    
    register_extensions(app)
    register_modules(app)
    register_default_route(app)

    return app
