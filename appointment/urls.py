from django.urls import path
from .views import AppointmentCreate
from . import views


urlpatterns = [
    path('appointment/<str:doctor>/',
         AppointmentCreate.as_view(), name='create-appointment'),
    path('appointment/details/<str:nm>/<int:hr>/<int:min>/',
         views.details, name='appoint_details')
]
