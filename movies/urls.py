from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('book/<int:movie_id>/', views.booking_form, name='booking_form'),
    path('confirmation/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),
]
