from django import forms
from django.forms import widgets
from .models import DoctorAppointment


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class DoctorAppointmentForm(forms.ModelForm):

    class Meta:
        model = DoctorAppointment
        fields = ['required_speciality',
                  'date_of_appointment', 'start_time_of_appointment']
        widgets = {'date_of_appointment': DateInput(
        ), 'start_time_of_appointment': TimeInput()}
