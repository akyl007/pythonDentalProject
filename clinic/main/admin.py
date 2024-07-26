from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Doctor, Appointment, Service, CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Service)
