from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('book_appointment/', views.book_appointment, name='book_appointment'),
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('report/<int:appointment_id>/', views.view_report, name='view_report'),
]
