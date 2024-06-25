from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass

class Appointment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f'{self.user.username} - {self.date} {self.time}'

class TestReport(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    report_file = models.FileField(upload_to='reports/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Report for {self.user.username} on {self.appointment.date}'

