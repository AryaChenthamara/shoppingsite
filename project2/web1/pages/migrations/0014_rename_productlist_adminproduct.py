# Generated by Django 4.2.5 on 2023-11-10 06:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0013_productlist"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Productlist",
            new_name="Adminproduct",
        ),
    ]
