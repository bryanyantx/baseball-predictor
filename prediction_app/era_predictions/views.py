from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import joblib
import numpy as np

def predict(model, input_data):
    prediction = model.predict(input_data)
    return prediction

@login_required(login_url='login')
def home(request):
    users = User.objects.all()

    model = joblib.load('era_predictions/ml_models/linear_regression.joblib')
    if request.method=='POST':
        user_input = []
        for i in range(1, 10):
            user_value = float(request.POST.get(f'input{i}'))
            user_input.append(user_value)

        prediction = model.predict([user_input])

        return render(request, 'era_predictions/home.html', {'users': users, 'prediction': prediction[0][0]})
    return render(request, 'era_predictions/home.html', {'users': users})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'era_predictions/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'era_predictions/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'era_predictions/register.html', {'form': form})
