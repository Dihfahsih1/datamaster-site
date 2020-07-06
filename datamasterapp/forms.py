from .models import *
from django import forms
from .models import *
from django.forms import Textarea, TextInput, ChoiceField
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, MonthPickerInput 
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('full_name','email','subject','comment')
        widgets = {
            'full_name': TextInput(attrs={'placeholder': 'Your Name'}),
            'email': TextInput(attrs={'placeholder': 'Your Email Address'}),
        } 