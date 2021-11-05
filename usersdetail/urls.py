from django.contrib import admin
from django.urls import path
from . import views
from .views import DoctorListView, ProfileDetailView

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('search/doctor/', views.autocompleteModel, name='search-doctor'),
    path('doctor/', DoctorListView.as_view(), name='doctor'),
    path('profile/<int:pk>/details',
         ProfileDetailView.as_view(), name='profile-detail'),
]
