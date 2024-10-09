from django.db import models
from users.models import User


class Profile(models.Model):
    GENDER_CHOICES = (
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    )
    MARITAL_STATUS_CHOICES = (
        ("single", "Single"),
        ("married", "Married"),
        ("divorced", "Divorced"),
        ("widowed", "Widowed"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES)
    temporary_address = models.CharField(max_length=255)
    temporary_city = models.CharField(max_length=100)
    temporary_state = models.CharField(max_length=100)
    temporary_country = models.CharField(max_length=100)
    temporary_zip_code = models.CharField(max_length=10)
    permanent_address = models.CharField(max_length=255)
    permanent_city = models.CharField(max_length=100)
    permanent_state = models.CharField(max_length=100)
    permanent_country = models.CharField(max_length=100)
    permanent_zip_code = models.CharField(max_length=10)
    passport_number = models.CharField(max_length=255)
    issue_date = models.DateField()
    expiry_date = models.DateField()
    issue_country = models.CharField(max_length=100)
    city_of_birth = models.CharField(max_length=100)
    country_of_birth = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    citizenship = models.CharField(max_length=100)
    emergency_contact_relationship = models.CharField(max_length=100)
    emergency_contact_phone = models.CharField(max_length=15)
    emergency_contact_email = models.EmailField(max_length=150)
    emergency_contact_name = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.user.full_name} Profile"

    class Meta:
        db_table = "profile"
        verbose_name_plural = "Profiles"
