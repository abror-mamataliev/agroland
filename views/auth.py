from flask import (
    flash,
    redirect,
    url_for
)
from flask_login import current_user

from forms import (
    LoginForm,
    RegisterForm
)
from models import (
    Profile,
    User
)
from lib.auth import login_user

from .base import BaseView


class AuthView(BaseView):

    __appname__: str = "auth"
    
    def get(self):
        user: User = current_user   # type: ignore
        if user.is_authenticated:
            return redirect(url_for("dashboard.index"))
        else:
            return super().get()


class LoginView(AuthView):

    def __init__(self, **kwargs):
        self._template: str = "login.html"
        self._forms: dict = {
            'loginform': LoginForm()
        }
        super().__init__(**kwargs)
    
    def post(self):
        loginform = LoginForm()
        if loginform.validate_on_submit():
            user: User = User.query.filter(
                User.email == loginform.email.data
            ).first()
            if user is None:
                flash("Bunday foydalanuvchi mavjud emas", "danger")
                return redirect(url_for("auth.login"))
            if not user.check_password(loginform.password.data):
                flash("Parol xato kiritilgan", "danger")
                return redirect(url_for("auth.login"))
            login_user(user, loginform.remember_me.data)
            flash("Platformaga muvaffaqiyatli kiritildi!", "success")
            return redirect(url_for("dashboard.index"))
        else:
            flash("Formani to'ldirishda xatolar mavjud", "danger")
            return redirect(url_for("auth.login"))


class RegisterView(AuthView):

    def __init__(self, **kwargs):
        self._template: str = "register.html"
        self._forms: dict = {
            'registerform': RegisterForm()
        }
        super().__init__(**kwargs)
    
    def post(self):
        registerform = RegisterForm()
        if registerform.validate_on_submit():
            user: User = User(
                email=registerform.email.data
            )
            user.set_password(registerform.password.data)
            user.save()
            profile: Profile = Profile(
                user_id=user.id
            )
            profile.save()
            login_user(user)
            flash("Platformaga muvaffaqiyatli kiritildi!", "success")
            return redirect(url_for("dashboard.index"))
        else:
            flash("Formani to'ldirishda xatolar mavjud", "danger")
            return redirect(url_for("auth.register"))


class LogoutView(AuthView):

    def get(self):
        from flask_login import logout_user

        user: User = current_user   # type: ignore
        if user.is_authenticated:
            logout_user()
        return redirect(url_for("auth.login"))
