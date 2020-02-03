from django import forms
from .models import *

class student_form(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    email = forms.CharField(widget=forms.EmailInput(), required=True, max_length=100)
    city = forms.CharField(widget=forms.TextInput(), required=False, max_length=100)
    marks = forms.CharField(widget=forms.NumberInput(), required=False, max_length=100 )


    class Meta():
        model = student
        fields = ['name', 'email', 'city', 'marks']