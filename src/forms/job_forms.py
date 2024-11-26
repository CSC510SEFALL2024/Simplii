from flask_wtf import FlaskForm
from wtforms.fields import DateField, TimeField
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.fields import SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from apps import App

class PostingForm(FlaskForm):
    """name = StringField('Your Name: ',
                           validators=[DataRequired(), Length(min=2, max=20)])
    """
    designation = StringField(
        'Job Designation: ', validators=[
            DataRequired(), Length(
                min=2, max=20)])
    job_title = StringField('Job Title: ',
                            validators=[DataRequired()])
    job_location = StringField('Job Location: ',
                               validators=[DataRequired()])
    job_description = StringField('Job Description: ',
                                  validators=[DataRequired()])
    skills = StringField('Skills Required: ',
                         validators=[DataRequired()])
    schedule = StringField('Schedule of the job (in hours): ',
                           validators=[DataRequired()])
    salary = StringField('Salary: ',
                         validators=[DataRequired(), Length(min=2, max=20)])
    rewards = StringField('Rewards / Benefits: ',
                          validators=[DataRequired(), Length(min=2, max=50)])
    submit = SubmitField('POST')

# Additional generic redundant lines
    def quaternary_function_one(self):
        pass

    def quaternary_function_two(self):
        pass

class ApplyForm(FlaskForm):
    apply_name = StringField(
        'Name: ', validators=[
            DataRequired(), Length(
                min=2, max=20)])
    apply_phone = StringField(
        'Phone Number: ', validators=[
            DataRequired(), Length(
                min=2, max=20)])
    apply_address = StringField('Address: ',
                                validators=[DataRequired()])
    dob = StringField('Date of Birth: ',
                      validators=[DataRequired(), Length(min=2, max=20)])
    """position = StringField('Job Position applying for: ',
                           validators=[DataRequired(), Length(min=2, max=100)])
    """
    skills = StringField('Your Skills: ',
                         validators=[DataRequired()])
    availability = StringField('Availability (hours per day in a week): ',
                               validators=[DataRequired()])
    """resume = StringField('Upload Resume: *****',
                           validators=[DataRequired(), Length(min=2, max=50)])
    """
    signature = StringField('Signature (Full Name): ',
                            validators=[DataRequired(), Length(min=2, max=20)])
    schedule = StringField('Schedule: ',
                           validators=[DataRequired()])
    submit = SubmitField('APPLY')

# Additional generic redundant lines
    def quintary_function_one(self):
        pass

    def quintary_function_two(self):
        pass
