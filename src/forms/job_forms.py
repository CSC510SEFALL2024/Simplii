from flask_wtf import FlaskForm
from .base_fields import (
    designation_field, job_title_field, job_location_field,
    job_description_field, skills_field, schedule_field,
    salary_field, rewards_field, submit_button
)

from .base_fields import (
    apply_name_field, apply_phone_field, apply_address_field,
    dob_field, skills_field, availability_field, signature_field,
    schedule_field, submit_button
)

class PostingForm(FlaskForm):
    designation = designation_field
    job_title = job_title_field
    job_location = job_location_field
    job_description = job_description_field
    skills = skills_field
    schedule = schedule_field
    salary = salary_field
    rewards = rewards_field
    submit = submit_button

class ApplyForm(FlaskForm):
    apply_name = apply_name_field
    apply_phone = apply_phone_field
    apply_address = apply_address_field
    dob = dob_field
    skills = skills_field
    availability = availability_field
    signature = signature_field
    schedule = schedule_field
    submit = submit_button