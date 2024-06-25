from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, AppointmentForm
from .models import Appointment, TestReport

def home(request):
    """
    Renders the home page.
    """
    return render(request, 'core/home.html')

def register(request):
    """
    Handles user registration.
    GET: Renders registration form.
    POST: Processes registration form submission.
    """
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
    """
    Allows logged-in users to book appointments.
    GET: Renders appointment booking form.
    POST: Processes appointment form submission.
    """
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            # Redirect to appointment list after successful booking
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    
    return render(request, 'core/book_appointment.html', {'form': form})

@login_required
def appointment_list(request):
    """
    Displays a list of appointments for the logged-in user.
    """
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'core/appointment_list.html', {'appointments': appointments})

@login_required
def view_report(request, appointment_id):
    """
    Allows users to view test reports associated with their appointments.
    """
    # Get the specific appointment related to the current user
    appointment = get_object_or_404(Appointment, id=appointment_id, user=request.user)
    
    # Try to retrieve the test report associated with the appointment
    try:
        report = TestReport.objects.get(appointment=appointment)
    except TestReport.DoesNotExist:
        report = None
    
    return render(request, 'core/view_report.html', {'appointment': appointment, 'report': report})
