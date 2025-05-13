from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add/', views.add_faculty, name='add_faculty'),
    path('edit/<int:pk>/', views.edit_faculty, name='edit_faculty'),
    path('delete/<int:pk>/', views.delete_faculty, name='delete_faculty'),
]