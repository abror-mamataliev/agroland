from modules import auth
from views import auth as auth_views


auth.add_url_rule("/login", view_func=auth_views.LoginView.as_view("login"))
auth.add_url_rule("/logout", view_func=auth_views.LogoutView.as_view("logout"))
auth.add_url_rule("/register", view_func=auth_views.RegisterView.as_view("register"))
