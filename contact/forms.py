from django import forms
from django.core.validators import RegexValidator

class ContactForm(forms.Form):
    CONTACT_METHOD_CHOICES = [
        ('email', 'Email'),
        ('phone', 'Phone'),
    ]
    
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(
        max_length=15, 
        required=False,
        validators=[
            RegexValidator(
                regex=r'^\+?\d{9,15}$',
                message="Please enter a valid phone number."
            )
        ]
    )

    message = forms.CharField(widget=forms.Textarea)