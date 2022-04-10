from email import message
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def user_registration(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account was created for {username}.')

            return redirect('login')
    else:
        print("Could not do anything")

    context = {'form': form}
    return render(request, 'registration.html', context)


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.add_message(request, messages.SUCCESS, f'Welcome back {username}')
            return redirect('students')
        else:
            messages.add_message(request, messages.WARNING, 'Username or password is incorrect.')
            return redirect('/')

    context = {}
    return render(request, 'login.html', context)


def user_logout(request):
    logout(request)
    print("You were logged out ... ")
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