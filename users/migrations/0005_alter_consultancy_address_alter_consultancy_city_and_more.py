# Generated by Django 5.1.1 on 2024-10-08 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_consultancy_phone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="consultancy",
            name="address",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="consultancy",
            name="city",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="consultancy",
            name="country",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="consultancy",
            name="phone",
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name="consultancy",
            name="state",
            field=models.CharField(
                choices=[
                    ("Province 1", "Province 1"),
                    ("Province 2", "Province 2"),
                    ("Bagmati", "Bagmati"),
                    ("Gandaki", "Gandaki"),
                    ("Lumbini", "Lumbini"),
                    ("Karnali", "Karnali"),
                    ("Sudurpashchim", "Sudurpashchim"),
                ],
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="consultancy",
            name="zip_code",
            field=models.CharField(max_length=10),
        ),
    ]