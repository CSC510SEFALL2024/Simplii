from flask_wtf import FlaskForm
from .base_fields import (
    taskname_field, category_field, startdate_field, duedate_field, reminder_date_field, reminder_time_field, priority_field,
    status_field, hours_field, submit_button
)
from .validators import validate_duedate

class TaskForm(FlaskForm):
    taskname = taskname_field
    category = category_field
    startdate = startdate_field
    duedate = duedate_field
    status = status_field
    hours = hours_field
    priority = priority_field
    submit = submit_button

    def validate_duedate(self, field):
        validate_duedate(self, field)

class UpdateForm(FlaskForm):
    taskname = taskname_field
    category = category_field
    startdate = startdate_field
    duedate = duedate_field
    status = status_field
    hours = hours_field
    submit = submit_button

    def validate_duedate(self, field):
        validate_duedate(self, field)

class ReminderForm(FlaskForm):
    taskname = taskname_field
    category = category_field
    startdate = startdate_field
    duedate = duedate_field
    status = status_field
    hours = hours_field
    reminder_date = reminder_date_field
    reminderTime = reminder_time_field
    submit = submit_button

    def validate_duedate(self, field):
        validate_duedate(self, field)