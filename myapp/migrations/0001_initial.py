# Generated by Django 4.1.6 on 2023-07-31 07:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='doctor_pictures')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('about_you', models.TextField()),
                ('registration_number', models.CharField(max_length=50)),
                ('document_upload', models.FileField(blank=True, null=True, upload_to='doctor_documents')),
                ('specialization', models.CharField(choices=[('Cardiologist', 'Cardiologist'), ('Dermatologist', 'Dermatologist'), ('Gynecologist', 'Gynecologist'), ('Pediatrician', 'Pediatrician'), ('Orthopedic', 'Orthopedic')], max_length=50)),
                ('card_name', models.CharField(max_length=255)),
                ('card_expiration_date', models.DateField()),
                ('cvv', models.CharField(max_length=4)),
                ('card_number', models.CharField(max_length=16)),
                ('payment_method', models.CharField(max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('available_time', models.TimeField()),
                ('unavailable_time', models.TimeField()),
                ('day_selection', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('full_name', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='patient_pictures')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('blood_type', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=3)),
                ('heart_rate', models.IntegerField()),
                ('blood_pressure', models.CharField(max_length=10)),
                ('glucose_level', models.FloatField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
