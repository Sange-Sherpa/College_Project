from django.urls import path
from .views import *

urlpatterns = [
    path('', user_login, name='login'),
    path('register/', user_registration, name='registration'),
    path('base/', base, name='base'),
    path('attendance/', attendance, name='attendance'),
    path('students/', students, name='students'),
    path('settings/', settings, name='settings'),
    path('logout/', user_logout, name='logout'),
]