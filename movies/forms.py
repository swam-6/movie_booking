from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['user_name', 'ticket_type', 'number_of_tickets']
        widgets = {
            'user_name': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
            'number_of_tickets': forms.NumberInput(attrs={'min': 1, 'max': 10}),
        }
