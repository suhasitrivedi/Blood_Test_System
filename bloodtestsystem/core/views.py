from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, AppointmentForm
from .models import Appointment, TestReport

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'core/register.html', {'form': form})

@login_required
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'core/book_appointment.html', {'form': form})

@login_required
def appointment_list(request):
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'core/appointment_list.html', {'appointments': appointments})

@login_required
def view_report(request, appointment_id):
    report = TestReport.objects.get(appointment_id=appointment_id, user=request.user)
    return render(request, 'core/view_report.html', {'report': report})
