from django.forms import ModelForm, TextInput
from .models import Doctor, Appointment , Services


class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = ["name", "login", "tel"]
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'login': TextInput(attrs={'class': 'form-control'}),
            'tel': TextInput(attrs={'class': 'form-control'}),
        }

class AppointmentForm(ModelForm):
       class Meta:
            model = Appointment
            fields = ["name", "phone"]
            widgets = {
                'name': TextInput(attrs={'class': 'form-control','required':'required'}),
                'phone': TextInput(attrs={'class': 'form-control','required':'required'}),
            }

class ServiceForm(ModelForm):
        class Meta:
            model = Services
            fields = ["name", "price"]
            widgets = {
                'name': TextInput(attrs={'class': 'form-control', 'required': 'required'}),
                'phone': TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            }