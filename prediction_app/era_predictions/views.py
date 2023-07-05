from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'era_predictions/home.html')

def login_view(request):
    if request.method == 'POST':
        # Handle login form submission
        # Authenticate user and log in
        pass
    else:
        # Render the login form
        return render(request, 'era_predictions/login.html')

@login_required
def logout_view(request):
    # Log out the user
    logout(request)
    return redirect('home')
