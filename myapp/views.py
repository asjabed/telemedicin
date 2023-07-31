from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import PatientRegistrationForm
from .forms import DoctorRegistrationForm



# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def blog(request):
    return render(request,'blog.html')


#blog soction
def blog_details(request):
    return render(request,'blog_details/blog_details1.html')

def blog_details2(request):
    return render(request,'blog_details/blog_details2.html')

def blog_details3(request):
    return render(request,'blog_details/blog_details3.html')

def blog_details4(request):
    return render(request,'blog_details/blog_details4.html')

#----end blog section-----


def contact(request):
    return render(request, 'contact.html')

def search(request):
    return render(request,'search.html')

def login(request):
    return render(request,'login.html')
    


#---------------patient----------------
def patient_register(request):
    return render(request,'patient/patient_register.html')

def register(request):
    return render(request,'register_success.html')

def patient_phone(request):
    return render(request,'patient/patient_phone.html')

def patient_email_otp(request):
    return render(request,'patient/patient_email_otp.html')

def patient_password(request):
    return render(request,'patient/patient_password.html')

def patient_add_profile(request):
    return render(request,'patient/patient_add_profile.html')

def patient_details(request):
    return render(request,'patient/patient_details.html')

def patient_index(request):
    return render(request, 'patient/patient_index.html')

def doctor_profile(request):
    return render(request,'patient/doctor_profile.html')

def booking(request):
    return render(request,'patient/booking.html')

def checkout(request):
    return render(request,'patient/checkout.html')

def booking_success(request):
    return render(request,'patient/booking_success.html')

def invoice(request):
    return render(request,'patient/invoice.html')

def profile_settings(request):
    return render(request,'patient/profile_settings.html')

def add_medical_record(request):
    return render(request,'patient/add_medical_record.html')

def p_change_password(request):
    return render(request,'patient/p_change_password.html')

def patient_chat(request):
    return render(request,'patient/patient_chat.html')


#----------------doctor------------------

def doctor_register(request):
    return render(request,'doctor/doctor_register.html')

def doctor_email_veri(requist):
    return render(requist,'doctor/doctor_email_veri.html')

def doctor_email_otp(requist):
    return render(requist,'doctor/doctor_email_otp.html')

def doctor_password(requist):
    return render(requist,'doctor/doctor_password.html')

def doctor_personalize(requist):
    return render(requist,'doctor/doctor_personalize.html')

def doctor_verifaction(requist):
    return render(requist,'doctor/doctor_verifaction.html')

def doctor_payment(requist):
    return render(requist,'doctor/doctor_payment.html')

def doctor_preferences(requist):
    return render(requist,'doctor/doctor_preferences.html')

def doctor_deshboard(requist):
    return render(requist,'doctor/doctor_dashboard.html')

def appointments(requist):
    return render(requist,'doctor/appointments.html')

def patient_profile(requist):
    return render(requist,'doctor/patient_profile.html')

def my_patients(requist):
    return render(requist,'doctor/my_patients.html')

def schedule_timings(requist):
    return render(requist,'doctor/schedule_timings.html')

def available_timings(requist):
    return render(requist,'doctor/available_timings.html')

def chat_doctor(requist):
    return render(requist,'doctor/chat_doctor.html')

def doctor_profile_settings(requist):
    return render(requist,'doctor/doctor_profile_settings.html')

def change_password(requist):
    return render(requist,'doctor/change_password.html')





# Authentication login and signupviews


#Patient Register

def patient_register(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('registration_success')
    else:
        form = PatientRegistrationForm()
    return render(request, 'registration.html', {'form': form})

#Doctor Register
def register_doctor(request):
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('registration_success')
    else:
        form = DoctorRegistrationForm()
    return render(request, 'doctor_registration.html', {'form': form})

def registration_success(request):
    return render(request, 'registration_success.html')


