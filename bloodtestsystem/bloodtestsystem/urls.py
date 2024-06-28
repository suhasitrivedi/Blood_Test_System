from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),  # Endpoint for user registration
    path('book_appointment/', views.book_appointment, name='book_appointment'),  # Endpoint for booking appointments
    path('appointments/', views.appointment_list, name='appointment_list'),  # Endpoint for listing appointments
    path('appointments/<int:appointment_id>/', views.view_report, name='view_report'),  # Endpoint for viewing report
    path('accounts/', include('django.contrib.auth.urls')),  # Include Django's built-in authentication URLs
    path('', RedirectView.as_view(url='/register/', permanent=False)),  # Redirect root URL to register page
]
