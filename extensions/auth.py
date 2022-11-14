from flask import Flask
from flask_login import LoginManager


login_manager: LoginManager = LoginManager()


def register_auth(app: Flask) -> None:
    from flask import (
        redirect,
        url_for
    )
    
    from models import User

    login_manager.init_app(app)

    @login_manager.user_loader
    def user_loader(id):
        return User.query.get(id)
    
    @login_manager.unauthorized_handler
    def unauthorized_handler():
        return redirect(url_for("auth.login"))
