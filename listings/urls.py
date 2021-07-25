from django.urls import path
from .views import reservation,get_booking_info

app_name='listings'


urlpatterns = [
    path('reservation/',reservation,name='reservations'),
    path('free_rooms/',get_booking_info,name='get_booking_info'),
]
