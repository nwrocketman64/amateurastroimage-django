from django import forms
from captcha.fields import CaptchaField

from .models import Request

class RequestForm(forms.ModelForm):
    """
    Request Form: Defines the form that appears in the contact page.
    """
    # Add Simple Captcha to the form.
    captcha = CaptchaField(label="ReCaptcha")

    class Meta:
        # Defines the model the form is based off of.
        model = Request

        # List the fields that should appear in the form.
        fields = [
            "first_name",
            "last_name",
            "email",
            "comment",
        ]

        # Define the labels for the form fields.
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "email": "Email",
            "comment": "Comments / Questions",
        }

        # Define some key error messages for each form fields.
        error_messages = {
            "first_name": {
                "required": "Your first name must not be empty",
                "max_length": "Please enter a shorter first name",
            },
            "last_name": {
                "required": "Your last name must not be empty",
                "max_length": "Please enter a shorter last name",
            },
            "email": {
                "required": "Your email is required",
                "max_length": "Please enter a shorter email",
            },
            "comment": {
                "required": "A comment or question is required",
            },
        }
