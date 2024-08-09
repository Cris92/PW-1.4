from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('booking/', views.booking_view, name='booking'),
    path('rooms/', views.rooms, name='rooms'),
    path('manage-booking/', views.manage_booking, name='manage_booking'),
]