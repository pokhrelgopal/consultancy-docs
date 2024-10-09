from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)
from django.utils import timezone
from django.utils.text import slugify


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("role", "admin")
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("consultancy", "Consultancy"),
        ("student", "Student"),
    )

    email = models.EmailField(verbose_name="email address", max_length=255, unique=True)
    full_name = models.CharField(max_length=255, blank=True)
    role = models.CharField(max_length=255, choices=ROLE_CHOICES, default="student")

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.full_name}"

    class Meta:
        db_table = "user"
        verbose_name_plural = "Users"


class Consultancy(models.Model):
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    )

    STATE_CHOICES = (
        ("Province 1", "Province 1"),
        ("Province 2", "Province 2"),
        ("Bagmati", "Bagmati"),
        ("Gandaki", "Gandaki"),
        ("Lumbini", "Lumbini"),
        ("Karnali", "Karnali"),
        ("Sudurpashchim", "Sudurpashchim"),
    )

    name = models.CharField(max_length=255, unique=True)
    company_email = models.EmailField(max_length=255, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    logo = models.ImageField(upload_to="consultancy", null=True, blank=True)
    website = models.URLField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    state = models.CharField(max_length=100, choices=STATE_CHOICES)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    whatsapp = models.CharField(max_length=15, null=True, blank=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Consultancy, self).save(*args, **kwargs)

    class Meta:
        db_table = "consultancy"
        verbose_name_plural = "Consultancies"
