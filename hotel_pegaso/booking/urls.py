from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    path('rooms/', views.room_list, name='rooms'),
    path('rooms/<int:pk>/', views.room_detail, name='room_detail'),
    path('rooms/<int:room_id>/select_dates/', views.select_dates, name='select_dates'),
    path('rooms/<int:room_id>/confirm_booking/', views.confirm_booking, name='confirm_booking'),
    path('rooms/<int:room_id>/complete_booking/', views.complete_booking, name='complete_booking'),
    path('booking/<str:booking_code>/download_pdf/', views.generate_pdf, name='download_pdf'),
    path('manage_booking/', views.manage_booking, name='manage_booking'),
    path('booking/<int:booking_id>/edit/', views.edit_booking_view, name='edit_booking_view'),
    path('booking/<int:booking_id>/update/', views.edit_booking_post, name='edit_booking_post'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)