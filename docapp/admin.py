from django.contrib import admin
from .models import Doctor, Appointment

# Register your models here.

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'contact_number', 'email', 'available')
    list_filter = ('specialization', 'available')
    search_fields = ('name', 'specialization', 'email')

@admin.register(Appointment)  
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'doctor', 'appointment_date', 'appointment_time', 'reason')
    list_filter = ('doctor', 'appointment_date')
    search_fields = ('patient_name', 'doctor__name', 'reason')
    date_hierarchy = 'appointment_date'  

    actions = ['mark_as_completed'] 
    def mark_as_completed(self, request, queryset):
        queryset.update(reason='Completed')  
    mark_as_completed.short_description = "Mark selected appointments as completed"