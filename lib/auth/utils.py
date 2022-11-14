from .types import User


def login_user(user: User, remember_me: bool = False) -> None:
    from datetime import datetime
    from flask_login import login_user as flask_login_user
    
    flask_login_user(user, remember_me)
    user.last_login = datetime.now()
    user.save()
