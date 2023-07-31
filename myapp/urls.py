from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('about/',views.about,name='about'),
    path('blog/',views.blog,name='blog'),
    
    # blog details 
    path('blog_details/',views.blog_details,name='blog_details1'),
    path('blog_details2/',views.blog_details2,name='blog_details2'),
    path('blog_details3/',views.blog_details3,name='blog_details3'),
    path('blog_details4/',views.blog_details4,name='blog_details4'),
    
    path('contact/',views.contact, name='contact'),
    path('search/',views.search,name='search'),
    path('login/',views.login, name='login'),
    
    #patient url section
    path('patient_register/',views.patient_register,name='patient_register'),
    path('registration_success/',views.registration_success, name='registration_success'),

    path('patient_phone/',views.patient_phone,name='patient_phone'),
    path('patient_email_otp/',views.patient_email_otp,name='patient_email_otp'),
    path('patient_password/',views.patient_password,name='patient_password'),
    path('patient_add_profile/',views.patient_add_profile,name='patient_add_profile'),
    path('patient_details/',views.patient_details,name='patient_details'),
    
    path('patient_index/',views.patient_index, name='patient_index'),
    path('doctor_profile/',views.doctor_profile, name='doctor_profile'),
    path('booking/',views.booking,name='booking'),
    path('checkout/',views.checkout,name='checkout'),
    path('booking_success/',views.booking_success,name='booking_success'),
    path('invoice/',views.invoice,name='invoice'),
    path('profile_settings/',views.profile_settings,name='profile_settings'),
    path('add_medical_record/',views.add_medical_record,name='add_medical_record'),
    path('p_change_password/',views.p_change_password, name='p_change_password'),
    path('patient_chat/',views.patient_chat,name='patient_chat'),
    
    
    #Doctor url Section
    path('doctor_register/',views.doctor_register,name='doctor_register'),
    path('doctor_email_veri/',views.doctor_email_veri,name='doctor_email_veri'),
    path('doctor_email_otp/',views.doctor_email_otp,name='doctor_email_otp'),
    path('doctor_password/',views.doctor_password,name='doctor_password'),
    path('doctor_personalize/',views.doctor_personalize,name='doctor_personalize'),
    path('doctor_verifaction/',views.doctor_verifaction,name='doctor_verifaction'),
    path('doctor_payment/',views.doctor_payment,name='doctor_payment'),
    path('doctor_preferences/',views.doctor_preferences,name='doctor_preferences'),
    
    
    
    path('doctor_dashboard/',views.doctor_deshboard,name='doctor_dashboard'),
    path('appointments/',views.appointments,name='appointments'),
    path('available_timings/',views.available_timings, name='available_timings'),
    path('patient_profile/',views.patient_profile,name='patient_profile'),
    path('my_patients/',views.my_patients, name='my_patients'),
    path('schedule_timings/',views.schedule_timings,name='schedule_timings'),
    path('chat_doctor/',views.chat_doctor,name='chat_doctor'),
    path('doctor_profile_settings/',views.doctor_profile_settings,name='doctor_profile_settings'),
    path('change_password/',views.change_password,name='change_password'),
]
