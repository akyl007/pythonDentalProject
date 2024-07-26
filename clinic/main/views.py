from django.contrib.auth import login
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import DoctorForm, AppointmentForm, Service


import clickatell

from .models import Appointment


def index(request):
    form = DoctorForm()
    data = {
        'form' : form
    }

    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about')
    else:
        form = DoctorForm()

    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def pricing(request):
    return render(request, 'main/pricing.html')
def appointment(request):
    form = AppointmentForm()
    formGet = Service.objects.all()
    error = ''
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.status = 'В обработке'
            appointment.save()
            return redirect('index2')
        else:
            error = 'Ошибка'

    if request.method == 'GET':
        formGet = Service.objects.all()

    data = {
        'formGet': formGet,
        'form': form,
        'error': error
    }

    return render(request, 'main/appointment.html',data)

def index2(request):
    return render(request, 'accountClient/index2.html')

@permission_required('app_name.can_publish_article')
def appointment_create(request):
    return render(request, 'main/appointment_create.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index2')  # Redirect to the client orders page or another page
        # If the form is not valid, re-render the form with errors
        return render(request, 'accountClient/signup.html',
                      {'form': form})
    else:
        # If the request is GET, create a blank form
        form = UserCreationForm()
        return render(request, 'accountClient/signup.html',
                      {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index2')  # Redirect to the client orders page or another page
    else:
        form = AuthenticationForm()
    return render(request, 'accountClient/login.html',
                  {'form': form})


def app_list(request):
    appointment =  Appointment.objects.all()

    data = {
        'appointment': appointment
    }

    return render(request, 'accountClient/appointment_list.html', data)
