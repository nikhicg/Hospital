from django.db import models
from usersdetail.models import CustomUser
# Create your models here.
from django.urls import reverse


class DoctorAppointment(models.Model):
    doctor = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='doctor_name')
    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    required_speciality = models.CharField(max_length=200)
    date_of_appointment = models.DateField()
    start_time_of_appointment = models.TimeField()
    end_time_of_appointment = models.TimeField()

    def __str__(self):
        return f'Appointment of {self.patient} by {self.doctor}'

    def get_absolute_url(self):
        return reverse('appoint_details', kwargs={'nm': self.doctor, 'hr': self.start_time_of_appointment.hour, 'min': self.start_time_of_appointment.minute})
