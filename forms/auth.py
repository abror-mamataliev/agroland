from flask_wtf import FlaskForm
from wtforms.fields import (
    BooleanField,
    PasswordField,
    EmailField,
    SubmitField
)
from wtforms.validators import (
    DataRequired,
    EqualTo,
    Length
)


class LoginForm(FlaskForm):

    email = EmailField("Elektron pochta", validators=[DataRequired()])
    password = PasswordField("Parol", validators=[DataRequired(), Length(min=8, max=20)])
    remember_me = BooleanField("Eslab qolish")
    submit = SubmitField("Kirish")


class RegisterForm(FlaskForm):

    email = EmailField("Elektron pochta", validators=[DataRequired()])
    password = PasswordField("Parol", validators=[DataRequired(), Length(min=8, max=20)])
    password_confirm = PasswordField("Parolni tasdiqlash", validators=[DataRequired(), Length(min=8, max=20), EqualTo("password")])
    submit = SubmitField("Ro'yhatdan o'tish")
