from django.forms import ModelForm, TextInput
from .models import Doctor, Appointment , Service


class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = ["name", "login", "phone"]
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'login': TextInput(attrs={'class': 'form-control'}),
            'phone': TextInput(attrs={'class': 'form-control'}),
        }

class AppointmentForm(ModelForm):
       class Meta:
            model = Appointment
            fields = ["name", "phone"]
            widgets = {
                'name': TextInput(attrs={'class': 'form-control','required':'required', 'placeholder':'Введите ваше имя'}),
                'phone': TextInput(attrs={'class': 'form-control','required':'required', 'placeholder' : 'Введите номер телефона'}),
            }

class ServiceForm(ModelForm):
        class Meta:
            model = Service
            fields = ["name", "price"]
            widgets = {
                'name': TextInput(attrs={'class': 'form-control', 'required': 'required'}),
                'phone': TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            }