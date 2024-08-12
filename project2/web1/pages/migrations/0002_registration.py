# Generated by Django 4.2.1 on 2023-08-17 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Registration",
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
                ("reg_name", models.CharField(max_length=225)),
                ("reg_email", models.EmailField(max_length=255)),
                ("reg_phonenumber", models.CharField(max_length=255)),
                ("reg_userid", models.CharField(max_length=255)),
                ("reg_password", models.CharField(max_length=255)),
            ],
        ),
    ]
