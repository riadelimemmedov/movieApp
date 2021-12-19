from django.urls import path
from .views import *

urlpatterns = [
    path('login/',loginView,name='login'),
    path('register/',registerView,name='register'),
    path('change_password/',changePasswordView,name='change_password'),
    path('logout/',logoutView,name='logout'),
    path('profile/',profileView,name='profile'),
    path('watch-list/',watchView,name='watchlist'),
]