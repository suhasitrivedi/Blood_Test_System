from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('core.urls')),
    path('book_appointment/', include('core.urls')),
    path('appointments/', include('core.urls')),
    path('report/<int:appointment_id>/', include('core.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', RedirectView.as_view(url='register/', permanent=False)),
]
