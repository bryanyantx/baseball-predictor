from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import joblib
import numpy as np
from era_predictions.models import Prediction

def predict(model, input_data):
    prediction = model.predict(input_data)
    return prediction

@login_required(login_url='login')
def home(request):
    users = User.objects.all()

    predictionlist = Prediction.objects.order_by('timestamp')[:10]

    model = joblib.load('era_predictions/ml_models/linear_regression.joblib')
    
    if request.method=='POST':
        user_input = []
        for i in range(1, 10):
            user_value = float(request.POST.get(f'input{i}'))
            user_input.append(user_value)

        prediction = model.predict([user_input])

        user = request.user
        new_prediction = Prediction(user=user, input1=user_input[0], input2=user_input[1], input3=user_input[2], input4=user_input[3], input5=user_input[4], input6=user_input[5], input7=user_input[6], input8=user_input[7], input9=user_input[8], output=prediction)
        new_prediction.save()

        return render(request, 'era_predictions/home.html', {'users': users, 'predictionlist': predictionlist, 'prediction': prediction[0][0]})
    return render(request, 'era_predictions/home.html', {'users': users, 'predictionlist': predictionlist})

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
