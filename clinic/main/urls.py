from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('about',views.about, name="about"),
    path('contacts',views.contacts, name="contacts"),
    path('pricing',views.pricing, name="pricing"),
    path('appointment',views.appointment, name="appointment"),
    path('appointment_create',views.appointment_create, name="appointment_create"),
    path('client',views.index2, name="index2"),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('appointment_list/', views.app_list, name='appointment_list'),

]
