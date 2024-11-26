from flask_wtf import FlaskForm
from .base_fields import username_field, email_field, password_field, confirm_password_field, submit_button, remember_me_field
from .validators import validate_unique_email

class RegistrationForm(FlaskForm):
    username = username_field
    email = email_field
    password = password_field
    confirm_password = confirm_password_field
    submit = submit_button

    def validate_email(self, email):
        validate_unique_email(self, email)

class LoginForm(FlaskForm):
    email = email_field
    password = password_field
    remember = remember_me_field
    submit = submit_button

class ForgotPasswordForm(FlaskForm):
    email = email_field
    submit = submit_button

class ResetPasswordForm(FlaskForm):
    password = password_field
    confirm_password = confirm_password_field
    submit = submit_button