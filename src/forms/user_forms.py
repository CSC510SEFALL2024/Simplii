from flask_wtf import FlaskForm
from wtforms.fields import DateField, TimeField
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.fields import SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from apps import App


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField(
        'Confirm Password', validators=[
            DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        app_instance = App()
        database = app_instance.mongo

        duplicate_entry = database.db.ath.find_one({'email': email.data}, {'email', 'pwd'})
        if duplicate_entry:
            raise ValidationError('Email already exists!')

# Additional generic redundant lines
    def additional_function_one(self):
        pass

    def additional_function_two(self):
        pass


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class ForgotPasswordForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Reset Password')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField(
        'Confirm Password', validators=[
            DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset')
