from wtforms import StringField, SelectField, DateField, PasswordField, BooleanField, SubmitField, TimeField
from wtforms.validators import DataRequired, Length, Email, EqualTo

#Task Fields
taskname_field = StringField(
    'Taskname',
    validators=[DataRequired(), Length(min=2, max=20)]
)

category_field = SelectField(
    'Category',
    choices=[
        ('', 'Select Category'),
        ('Intellectual', 'Intellectual'),
        ('Physical', 'Physical')
    ],
    validators=[DataRequired()]
)

status_field = SelectField(
    'Status',
    choices=[
        ('', 'Select Status'),
        ('To-Do', 'To-Do'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done')
    ],
    validators=[DataRequired()]
)

startdate_field = DateField('Start Date', format='%Y-%m-%d')

duedate_field = DateField('Due Date', format='%Y-%m-%d')

hours_field = StringField(
    'Hours Required',
    validators=[DataRequired(), Length(min=1, max=20)]
)

reminder_time_field = TimeField('Reminder Time')

reminder_date_field = DateField(
    'Reminder date',
    format='%Y-%m-%d'
)

#User Fields
username_field = StringField(
    'Username',
    validators=[DataRequired(), Length(min=2, max=20)]
)
email_field = StringField(
    'Email',
    validators=[DataRequired(), Email()]
)

password_field = PasswordField(
    'Password',
    validators=[DataRequired()]
)

confirm_password_field = PasswordField(
    'Confirm Password',
    validators=[DataRequired(), EqualTo('password')]
)

submit_button = SubmitField('Submit')

remember_me_field = BooleanField('Remember Me')

#Job Fields
designation_field = StringField(
    'Job Designation: ',
    validators=[DataRequired(), Length(min=2, max=20)]
)

job_title_field = StringField(
    'Job Title: ',
    validators=[DataRequired()]
)

job_location_field = StringField(
    'Job Location: ',
    validators=[DataRequired()]
)

job_description_field = StringField(
    'Job Description: ',
    validators=[DataRequired()]
)

skills_field = StringField(
    'Skills Required: ',
    validators=[DataRequired()]
)

schedule_field = StringField(
    'Schedule of the job (in hours): ',
    validators=[DataRequired()]
)

salary_field = StringField(
    'Salary: ',
    validators=[DataRequired(), Length(min=2, max=20)]
)

rewards_field = StringField(
    'Rewards / Benefits: ',
    validators=[DataRequired(), Length(min=2, max=50)]
)

apply_name_field = StringField(
    'Name: ',
    validators=[DataRequired(), Length(min=2, max=20)]
)

apply_phone_field = StringField(
    'Phone Number: ',
    validators=[DataRequired(), Length(min=2, max=20)]
)

apply_address_field = StringField(
    'Address: ',
    validators=[DataRequired()]
)

dob_field = StringField(
    'Date of Birth: ',
    validators=[DataRequired(), Length(min=2, max=20)]
)

availability_field = StringField(
    'Availability (hours per day in a week): ',
    validators=[DataRequired()]
)

signature_field = StringField(
    'Signature (Full Name): ',
    validators=[DataRequired(), Length(min=2, max=20)]
)

