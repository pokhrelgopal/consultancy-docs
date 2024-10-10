# Generated by Django 5.1.1 on 2024-10-10 04:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0006_alter_education_unique_together"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Document",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "document",
                    models.CharField(
                        choices=[
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
                            (
                                "ward_document_relationship",
                                "Ward Document Relationship",
                            ),
                            (
                                "ward_documents_annual_income",
                                "Ward Documents Annual Income",
                            ),
                            (
                                "ward_documents_tax_clearance",
                                "Ward Documents Tax Clearance",
                            ),
                            ("salary_certificate", "Salary Certificate"),
                            ("land_lease_agreement", "Land Lease Agreement"),
                            ("property_valuation", "Property Valuation"),
                            ("lalpurja", "Lalpurja"),
                            ("bank_statement", "Bank Statement"),
                            ("academic_documents", "Academic Documents"),
                            ("others", "Others"),
                        ],
                        max_length=50,
                    ),
                ),
                ("document_file", models.FileField(upload_to="documents/")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("approved", "Approved"),
                            ("rejected", "Rejected"),
                        ],
                        default="pending",
                        max_length=10,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="documents",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Documents",
                "db_table": "document",
                "ordering": ["-created_at"],
                "unique_together": {("user", "document")},
            },
        ),
    ]
