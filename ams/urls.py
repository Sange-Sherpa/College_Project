from django.urls import path
from .views import *

urlpatterns = [
    path('', login, name='login'),
    path('register', registration, name='registration'),
    path('base/', base, name='base'),
    path('attendance/', attendance, name='attendance'),
    path('students/', students, name='students'),
    path('settings/', settings, name='settings'),
    path('logout/', logout, name='logout'),
]