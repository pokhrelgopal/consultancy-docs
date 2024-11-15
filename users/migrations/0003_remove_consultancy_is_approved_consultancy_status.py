# Generated by Django 5.1.1 on 2024-10-08 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_consultancy"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="consultancy",
            name="is_approved",
        ),
        migrations.AddField(
            model_name="consultancy",
            name="status",
            field=models.CharField(
                choices=[
                    ("pending", "Pending"),
                    ("approved", "Approved"),
                    ("rejected", "Rejected"),
                ],
                default="pending",
                max_length=100,
            ),
        ),
    ]
