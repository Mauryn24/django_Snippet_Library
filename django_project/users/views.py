# Importing necessary modules and classes from Django
from django.shortcuts import render, redirect  # Importing render and redirect functions from Django shortcuts
from django.contrib import messages  # Importing messages module from Django contrib
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm  # Importing the UserRegisterForm from the current directory's forms module


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
            messages.success(request, f'Your account has been created! You are now able to login')
            # Redirect the user to the blog home page
            return redirect('login')
    else:
        # If it's not a POST request, create a new instance of UserRegisterForm
        form = UserRegistrationForm()
    # Render the register.html template with the form data
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        # create instances
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been update!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    # DO NOT FORGET TO PASS THE context TO THE TEMPLATE
    return render(request, 'users/profile.html', context)

