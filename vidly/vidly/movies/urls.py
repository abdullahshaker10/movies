from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('insert/', views.addMovie, name='insert'),
    path('show/<movie_id>', views.details, name='detail'),

]
