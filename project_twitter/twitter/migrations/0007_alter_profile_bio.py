# Generated by Django 5.1.4 on 2025-02-14 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("twitter", "0006_alter_profile_bio"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="bio",
            field=models.CharField(default="Ola, Sou novo aqui!", max_length=100),
        ),
    ]
