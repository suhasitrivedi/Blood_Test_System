from django.contrib import admin
from django.urls import path
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site URL
    path('register/', core_views.register, name='register'),  # Register view
    path('book_appointment/', core_views.book_appointment, name='book_appointment'),  # Book appointment view
    path('appointments/', core_views.appointment_list, name='appointment_list'),  # List appointments view
    path('report/<int:appointment_id>/', core_views.view_report, name='view_report'),  # View report for specific appointment
    path('', core_views.home, name='home'),  # Home page view
]
