from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

# Create your models here.
class usersignup(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    username=models.EmailField()
    password=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    mobile=models.BigIntegerField()

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    patient_name = models.CharField(max_length=100)
    patient_email = models.EmailField()
    appointment_date = models.DateField(validators=[MinValueValidator(timezone.now().date())])
    appointment_time = models.TimeField()
    reason = models.TextField()

    def __str__(self):
        return f"Appointment for {self.patient_name} with Dr. {self.doctor.name} on {self.appointment_date} at {self.appointment_time}"


