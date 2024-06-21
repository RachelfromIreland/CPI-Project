from django import forms
from .models import Booking
from django.utils import timezone
from datetime import timedelta

class BookingForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Date',
        validators=[
            lambda date: date >= (timezone.now() + timedelta(days=1)).date()
        ]
    )

    class Meta:
        model = Booking
        fields = ['booking_name', 'num_attending', 'date', 'time_slot']