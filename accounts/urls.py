from django.urls import path
from .views import login_customs, register_view

url_pattersns = [
    path('login/', login_customs, name='login'),
    path('register/', register_view, name='register'),
]