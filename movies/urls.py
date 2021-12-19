from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('movies/',movies,name='movies'),
    path('movies/<slug:slug>/',movie_details,name='moviedetail')
]