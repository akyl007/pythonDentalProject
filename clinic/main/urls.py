from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('about',views.about, name="about"),
    path('contacts',views.contacts, name="contacts"),
    path('pricing',views.pricing, name="pricing"),
    path('appointment',views.appointment, name="appointment"),
    path('appointment_create',views.appointment_create, name="appointment_create"),

]
