from django.db import models
from django.contrib.auth.models import User

#Patient
class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    BLOOD_TYPE_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    full_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    picture = models.ImageField(upload_to='patient_pictures', blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPE_CHOICES)
    heart_rate = models.IntegerField()
    blood_pressure = models.CharField(max_length=10)
    glucose_level = models.FloatField()

    def __str__(self):
        return self.full_name


# Doctor 
class Doctor(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    SPECIALIZATION_CHOICES = [
        ('Cardiologist', 'Cardiologist'),
        ('Dermatologist', 'Dermatologist'),
        ('Gynecologist', 'Gynecologist'),
        ('Pediatrician', 'Pediatrician'),
        ('Orthopedic', 'Orthopedic'),
        # Add more specialization choices as needed
    ]

    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    picture = models.ImageField(upload_to='doctor_pictures', blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    about_you = models.TextField()
    registration_number = models.CharField(max_length=50)
    document_upload = models.FileField(upload_to='doctor_documents', blank=True, null=True)
    specialization = models.CharField(max_length=50, choices=SPECIALIZATION_CHOICES)
    card_name = models.CharField(max_length=255)
    card_expiration_date = models.DateField()
    cvv = models.CharField(max_length=4)
    card_number = models.CharField(max_length=16)
    payment_method = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    available_time = models.TimeField()
    unavailable_time = models.TimeField()
    day_selection = models.CharField(max_length=20)

    def __str__(self):
        return self.name
