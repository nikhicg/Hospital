from django.contrib import admin
from django.urls import path
from . import views
from .views import PostCreateView, PostListView, PostUpdateView, PostDetailView, PostDeleteView, FieldPostListView, DraftListView
urlpatterns = [
    path('post/create/', PostCreateView.as_view(), name='post-create'),
    path('', PostListView.as_view(), name='post-list'),
    path('post/search/', views.autocompleteModel, name='search'),
    path('post/<slug:slug>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/detail/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<slug:slug>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<slug:slug>/', FieldPostListView.as_view(), name='user-field-posts'),
    path('<slug:slug>/draft/', DraftListView.as_view(), name='draft'),
]
