from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from django.http import HttpResponse

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            UserProfile.objects.create(user=user)
            login(request, user)
            return redirect('home')  # Redirect to home view after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'logins/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home view after successful login
        else:
            return render(request, 'logins/login.html', {'error': 'Invalid username or password'})
    return render(request, 'logins/login.html')
from django.shortcuts import render
from django.http import HttpResponse

def user_logout(request):
    logout(request)
    return redirect('home')  # Redirect to home view after logout

## Luis testing:
def logins(request):
    return HttpResponse("Hello, this will handle all the logins!") 
