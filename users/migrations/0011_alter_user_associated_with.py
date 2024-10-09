# Generated by Django 5.1.1 on 2024-10-09 11:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0010_alter_user_associated_with"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="associated_with",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="students",
                to="users.consultancy",
            ),
        ),
    ]
