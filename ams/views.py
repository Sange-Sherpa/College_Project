from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html')

def registration(request):
    return render(request, 'registration.html')

def base(request):
    return render(request, 'base.html')

def attendance(request):
    return render(request, 'pages/attendance.html')

def students(request):
    return render(request, 'pages/students.html')

def settings(request):
    return render(request, 'pages/settings.html')

def logout(request):
    return render(request, 'pages/logout.html')