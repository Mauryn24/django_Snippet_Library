# Importing necessary modules and classes from Django
from django.shortcuts import render, redirect  # Importing render and redirect functions from Django shortcuts
from django.contrib.auth.forms import UserCreationForm  # Importing the UserCreationForm from Django auth forms
from django.contrib import messages  # Importing messages module from Django contrib

# Create your views here.
def register(request):
    # Check if it's a POST request to create forms
    if request.method == 'POST':
        # If it's a POST request, initialize the UserCreationForm with the POST data
        form = UserCreationForm(request.POST)
        # Check if the form is valid
        if form.is_valid():
            # If the form is valid, get the username from the form data
            username = form.cleaned_data.get('username')
            # Display a success message to the user
            messages.success(request, f'Account created for {username}!')
            # Redirect the user to the blog home page
            return redirect('blog-home')
    else:
        # If it's not a POST request, create a new instance of UserCreationForm
        form = UserCreationForm()
    # Render the register.html template with the form data
    return render(request, 'users/register.html', {'form': form})
