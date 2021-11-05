from __future__ import print_function
from django.db.models import fields
from django.db.models.fields import CharField
from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import DoctorAppointmentForm
from Blog import models
from .models import DoctorAppointment
from usersdetail.models import CustomUser
import datetime as dati
from datetime import datetime, timedelta
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


class AppointmentCreate(LoginRequiredMixin, CreateView):
    form_class = DoctorAppointmentForm
    template_name = 'appointment/create_appoint.html'

    def form_valid(self, form):
        ad = CustomUser.objects.get(
            username=self.kwargs.get('doctor'))
        form.instance.doctor = CustomUser.objects.get(
            username=self.kwargs.get('doctor'))
        form.instance.patient = self.request.user
        dte = form.instance.date_of_appointment
        time = form.instance.start_time_of_appointment
        hr = time.hour
        min = time.minute
        min = min+45
        if min > 60:
            t = min-60
            hr = hr+1
            min = t
            dt = dati.time(hr, min, 0)
            form.instance.end_time_of_appointment = dt
        else:
            dt = dati.time(hr, min, 0)
            form.instance.end_time_of_appointment = dt

        SCOPES = ['https://www.googleapis.com/auth/calendar']
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'appointment/credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        service = build('calendar', 'v3', credentials=creds)
        start_time = datetime(
            dte.year, dte.month, dte.day, time.hour, time.minute)
        start_time = start_time.isoformat()
        end_time = datetime(
            year=dte.year, month=dte.month, day=dte.day, hour=dt.hour, minute=dt.minute)
        end_time = end_time.isoformat()
        print(start_time)
        event = {
            'summary': 'Doctor Appointment',
            'description': 'Appointment for'+str(self.request.user),
            'start': {
                'dateTime': start_time,
                'timeZone': 'Asia/Kolkata',
            },
            'end': {
                'dateTime': end_time,
                'timeZone': 'Asia/Kolkata',
            },
            'attendees': [
                {'email': str(ad.email_id)},
            ],
        }

        event = service.events().insert(calendarId='primary', body=event).execute()
        print('Event created: %s' % (event.get('htmlLink')))
        return super().form_valid(form)


def details(request, **kwargs):
    hr = kwargs['hr']
    min = kwargs['min']
    dt = dati.time(hr, min)
    c = CustomUser.objects.get(username=kwargs['nm'])
    a = DoctorAppointment.objects.filter(
        doctor=c, start_time_of_appointment=dt)
    context = {'a': a}
    print(a)
    return render(request, 'appointment/detail.html', context)
