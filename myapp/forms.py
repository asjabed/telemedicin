from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Patient
from .models import Doctor


class PatientRegistrationForm(UserCreationForm):
    # email = forms.EmailField(required=True)
    # picture = forms.ImageField(required=False)
    # gender = forms.ChoiceField(choices=Patient.GENDER_CHOICES)
    # blood_type = forms.ChoiceField(choices=Patient.BLOOD_TYPE_CHOICES)

    class Meta:
        model = Patient
        fields = "__all__"
        # (
        #     'first_name',
        #     'last_name',
        #     'full_name',
        #     'mobile',
        #     'email',
        #     'password1',
        #     'password2',
        #     'picture',
        #     'gender',
        #     'blood_type',
        #     'heart_rate',
        #     'blood_pressure',
        #     'glucose_level',
        # )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email address is already registered.")
        return email
    
    
# Doctor Regi_form

class DoctorRegistrationForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    picture = forms.ImageField(required=False)
    gender = forms.ChoiceField(choices=Patient.GENDER_CHOICES)
    
    class Meta:
        model = Doctor
        fields = (
            'name',
            'mobile',
            'email',
            'picture',
            'gender',
            'address',
            'city',
            'date_of_birth',
            'about_you',
            'registration_number',
            'document_upload',
            'specialization',
            'card_name',
            'card_expiration_date',
            'cvv',
            'card_number',
            'payment_method',
            'amount',
            'available_time',
            'unavailable_time',
            'day_selection',
        )
