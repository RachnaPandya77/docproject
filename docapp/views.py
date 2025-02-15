from django.shortcuts import render,  get_object_or_404, redirect
from .forms import *
from .models import Doctor, Appointment
from django.contrib.auth import logout


# Create your views here.

def index(request):
    msg=""
    if request.method=='POST':
        unm=request.POST['username'] 
        pas=request.POST['password']

        user=usersignup.objects.filter(username=unm,password=pas)
        if user:#true
            print("Login Successfull")
            request.session['user']=unm #session
            return redirect('profile')
        else:
            print("Error , Login Faild")
            msg="Error , Login Faild"
    return render(request,'index.html',{'msg':msg})

def profile(request):
    doctors = Doctor.objects.all()  # Fetch all doctors
    #print(doctors)
    return render(request, 'profile.html', {'doctors': doctors})

def contact(request):
    return render(request,'contact.html')

def signup(request):
    msg=""
    if request.method=='POST':
        newuser=signupform(request.POST)
        if newuser.is_valid():
            newuser.save()
            return redirect('/')
        else:
            print(newuser.errors)
            msg="Error , Something went wrong"
    return render(request,'signup.html',{'msg':msg})


def userlogout(request):
    logout(request)
    return redirect('/')


# Create a new doctor profile
def create_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = DoctorForm()
    return render(request, 'doctor_form.html', {'form': form})

# Update a doctor profile
def update_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'doctor_form.html', {'form': form})

# Delete a doctor profile
def delete_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('profile')
    return render(request, 'doctor_confirm_delete.html', {'doctor': doctor})


def book_appointment(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.doctor = doctor
            appointment.save()
            return redirect('profile')
    else:
        form = AppointmentForm()
    return render(request, 'book_appointment.html', {'form': form, 'doctor': doctor})



