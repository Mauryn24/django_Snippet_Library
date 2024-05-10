from django import forms  # Importing forms module from Django
from django.contrib.auth.models import User  # Importing User model from Django auth models
from django.contrib.auth.forms import UserCreationForm  # Importing UserCreationForm from Django auth forms
from .models import Profile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()  # Adding an email field to the form

    class Meta:
        model = User  # Specifying the User model for the form
        fields = ['username', 'email', 'password1', 'password2']  # Defining the fields for the form


#  create a model form
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()  # Adding an email field to the form

    class Meta:
        model = User  # Specifying the User model for the form
        fields = ['username', 'email']  # Defining the fields for the form

class ProfileUpdateForm(forms.ModelForm):
     class Meta:
        model = Profile  # Specifying the Profile model for the form
        fields = ['image']  # Defining the fields for the form
