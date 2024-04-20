# Importing necessary modules and classes from Django
from django.shortcuts import render, redirect  # Importing render and redirect functions from Django shortcuts
from django.contrib import messages  # Importing messages module from Django contrib
from .forms import UserRegistrationForm  # Importing the UserRegisterForm from the current directory's forms module


def register(request):
    # Check if the request method is POST
    if request.method == 'POST':
        # If it's a POST request, initialize the UserRegisterForm with the POST data
        form = UserRegistrationForm(request.POST)
        # Check if the form is valid
        if form.is_valid():
            # If the form is valid, save the form data to the database
            form.save()
            # Get the username from the form data
            username = form.cleaned_data.get('username')
            # Display a success message to the user
            messages.success(request, f'Account created for {username}!')
            # Redirect the user to the blog home page
            return redirect('blog-home')
    else:
        # If it's not a POST request, create a new instance of UserRegisterForm
        form = UserRegistrationForm()
    # Render the register.html template with the form data
    return render(request, 'users/register.html', {'form': form})
