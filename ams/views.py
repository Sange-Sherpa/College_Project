from .forms import CustomUserCreationForm
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def user_registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
    
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('students')

    else:
        form = CustomUserCreationForm()

    return render(request, 'registration.html', {'form': form})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print("Logged in !!")
            return redirect('students')
        else:
            print(user)
            return render(request, 'login.html', {'form': CustomUserCreationForm(request.POST)})
    
    else:
        return render(request, 'login.html', {'form': CustomUserCreationForm()})


def user_logout(request):
    logout(request)
    messages.success(request, "You were logged out ... ")
    return redirect('login')


def base(request):
    return render(request, 'base.html')


@login_required(login_url='login')
def attendance(request):
    return render(request, 'pages/attendance.html')


@login_required(login_url='login')
def students(request):
    return render(request, 'pages/students.html')


@login_required(login_url='login')
def settings(request):
    return render(request, 'pages/settings.html')