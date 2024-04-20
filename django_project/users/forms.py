from django import forms  # Importing forms module from Django
from django.contrib.auth.models import User  # Importing User model from Django auth models
from django.contrib.auth.forms import UserCreationForm  # Importing UserCreationForm from Django auth forms

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()  # Adding an email field to the form

    class Meta:
        model = User  # Specifying the User model for the form
        fields = ['username', 'email', 'password1', 'password2']  # Defining the fields for the form
