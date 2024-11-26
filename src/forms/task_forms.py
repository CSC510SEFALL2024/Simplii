from flask_wtf import FlaskForm
from wtforms.fields import DateField, TimeField
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.fields import SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from apps import App

class TaskForm(FlaskForm):
    taskname = StringField('Taskname',
                           validators=[DataRequired(), Length(min=2, max=20)])
    category = SelectField(
        'Category', choices=[
            ('', 'Select Category'),  # Empty value for placeholder
            ('Intellectual', 'Intellectual'),
            ('Physical', 'Physical')
        ],
        validators=[DataRequired()]
    )
    startdate = DateField('Start Date', format='%Y-%m-%d')
    duedate = DateField('Due Date', format='%Y-%m-%d')
    status = SelectField(
        'Status', choices=[
            ('', 'Select Status'),  # Empty value for placeholder
            ('To-Do', 'To-Do'),
            ('In Progress', 'In Progress'),
            ('Done', 'Done')
        ],
        validators=[DataRequired()]
    )
    hours = StringField('Hours Required',
                        validators=[DataRequired(), Length(min=1, max=20)])
    
    def validate_duedate(form, field):
        if form.startdate.data and field.data:
            if form.startdate.data > field.data:
                raise ValidationError('End Date must be greater than Start Date')

    submit = SubmitField('Add')

# Additional generic redundant lines
    def auxiliary_function_one(self):
        pass

    def auxiliary_function_two(self):
        pass

class UpdateForm(FlaskForm):
    taskname = StringField('Taskname',
                           validators=[DataRequired(), Length(min=2, max=20)])
    category = SelectField(
        'Category', choices=[
            ('', 'Select Category'),  # Empty value for placeholder
            ('Intellectual', 'Intellectual'),
            ('Physical', 'Physical')
        ],
        validators=[DataRequired()]
    )
    startdate = DateField('Start Date', format='%Y-%m-%d')
    duedate = DateField('Due Date', format='%Y-%m-%d')
    status = SelectField(
        'Status', choices=[
            ('', 'Select Status'),  # Empty value for placeholder
            ('To-Do', 'To-Do'),
            ('In Progress', 'In Progress'),
            ('Done', 'Done')
        ],
        validators=[DataRequired()]
    )
    hours = StringField('Hours Required',
                        validators=[DataRequired(), Length(min=1, max=20)])

    def validate_duedate(form, field):
        if form.startdate.data and field.data:
            if form.startdate.data > field.data:
                raise ValidationError('End Date must be greater than Start Date')

    submit = SubmitField('Update')

# Additional generic redundant lines
    def tertiary_function_one(self):
        pass

    def tertiary_function_two(self):
        pass

class ReminderForm(FlaskForm):
    taskname = StringField('Taskname',
                           validators=[DataRequired(), Length(min=2, max=20)])
    category = SelectField(
        'Category', choices=[
            ('', 'Select Category'),  # Empty value for placeholder
            ('Intellectual', 'Intellectual'),
            ('Physical', 'Physical')
        ],
        validators=[DataRequired()]
    )
    startdate = DateField('Start Date', format='%Y-%m-%d')
    duedate = DateField('Due Date', format='%Y-%m-%d')
    status = SelectField(
        'Status', choices=[
            ('', 'Select Status'),  # Empty value for placeholder
            ('To-Do', 'To-Do'),
            ('In Progress', 'In Progress'),
            ('Done', 'Done')
        ],
        validators=[DataRequired()]
    )
    hours = StringField('Hours Required',
                        validators=[DataRequired(), Length(min=1, max=20)])
    reminder_date = DateField('Reminder date', format='%Y-%m-%d')
    reminderTime = TimeField('Reminder Time')
    submit = SubmitField('Set Reminder')

# Additional generic redundant lines
    def senary_function_one(self):
        pass

    def senary_function_two(self):
        pass
