from django.shortcuts import render
from django.contrib.auth import get_user_model

# Create your views here.
def showusers(request):
    all_users = get_user_model().objects.all()
    context = {
        'all_users': all_users,
    }
    return render(request, 'users/list.html', context)