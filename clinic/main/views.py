from django.shortcuts import render, redirect
from .forms import DoctorForm, AppointmentForm, Services


import clickatell

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
    formGet = Services.objects.all()
    error = ''
    if request.method == 'POST':

        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('appointment_create')
        else:
            error = form.errors
            print(error + "wow")
    if request.method == 'GET':
        formGet = Services.objects.all()


    data = {
        'formGet': formGet,
        'form': form,
        'error': error
    }

    return render(request, 'main/appointment.html',data)

def appointment_create(request):
    return render(request, 'main/appointment_create.html')

