from wtforms.validators import ValidationError
from apps import App

def validate_unique_email(form, email):
    app_instance = App()
    database = app_instance.mongo

    duplicate_entry = database.db.ath.find_one({'email': email.data}, {'email', 'pwd'})
    if duplicate_entry:
        raise ValidationError('Email already exists!')

def validate_duedate(form, field):
    if form.startdate.data and field.data:
        if form.startdate.data > field.data:
            raise ValidationError('End Date must be greater than Start Date')
