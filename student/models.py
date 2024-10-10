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


class Education(models.Model):
    LEVEL_CHOICES = (
        ("grade 12 or equivalent", "Grade 12 or equivalent"),
        ("undergraduate", "Undergraduate"),
        ("postgraduate", "Postgraduate"),
    )
    GPA_SYSTEM_CHOICES = (
        ("4.0", "4.0"),
        ("5.0", "5.0"),
        ("7.0", "7.0"),
        ("10.0", "10.0"),
        ("100.0", "100.0"),
    )
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    level = models.CharField(max_length=50, choices=LEVEL_CHOICES)
    university_name = models.CharField(max_length=255)
    qualification_achieved = models.CharField(max_length=255)
    gpa_system = models.CharField(max_length=10, choices=GPA_SYSTEM_CHOICES)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    backlogs = models.PositiveIntegerField(null=True, blank=True, default=0)
    language = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="education")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.full_name} Education"

    class Meta:
        db_table = "education"
        verbose_name_plural = "Education"
        unique_together = ("user", "level")


class LanguageTest(models.Model):
    TEST_CHOICES = (
        ("ielts", "IELTS"),
        ("toefl", "TOEFL"),
        ("pte", "PTE"),
        ("gre", "GRE"),
        ("gmat", "GMAT"),
        ("sat", "SAT"),
        ("jlpt", "JLPT"),
        ("korean language", "Korean Language"),
    )
    test = models.CharField(max_length=20, choices=TEST_CHOICES)
    score = models.DecimalField(max_digits=6, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="test_scores")
    test_document = models.FileField(upload_to="test_documents/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.full_name} {self.test} Test Score"

    class Meta:
        db_table = "language_test"
        verbose_name_plural = "Language Tests"
        unique_together = ("user", "test")


class Document(models.Model):
    DOCUMENT_CHOICES = (
        ("application_form", "Application Form"),
        ("university_documents", "University Documents"),
        ("business_registration", "Business Registration"),
        ("passport_copy", "Passport Copy"),
        ("visa_request_letter", "Visa Request Letter"),
        ("statement_of_purpose", "Statement of Purpose"),
        ("moe", "MOE"),
        ("character_certificate", "Character Certificate"),
        ("ielts", "IELTS"),
        ("noc_swift", "NOC/Swift"),
        ("medical_report", "Medical Report"),
        ("sponsorship_letter", "Sponsorship Letter"),
        ("ca_report", "CA Report"),
        ("ward_document_relationship", "Ward Document Relationship"),
        ("ward_documents_annual_income", "Ward Documents Annual Income"),
        ("ward_documents_tax_clearance", "Ward Documents Tax Clearance"),
        ("salary_certificate", "Salary Certificate"),
        ("land_lease_agreement", "Land Lease Agreement"),
        ("property_valuation", "Property Valuation"),
        ("lalpurja", "Lalpurja"),
        ("bank_statement", "Bank Statement"),
        ("academic_documents", "Academic Documents"),
        ("others", "Others"),
    )
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    )
    UPLOADER_CHOICES = (
        ("self", "Self"),
        ("consultancy", "Consultancy"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="documents")
    document = models.CharField(max_length=50, choices=DOCUMENT_CHOICES)
    document_file = models.FileField(upload_to="documents/")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    uploader = models.CharField(max_length=20, choices=UPLOADER_CHOICES, default="self")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.full_name} {self.document}"

    class Meta:
        db_table = "document"
        verbose_name_plural = "Documents"
        ordering = ["-created_at"]
        unique_together = ("user", "document")
