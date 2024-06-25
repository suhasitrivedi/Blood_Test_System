from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Appointment

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'time']