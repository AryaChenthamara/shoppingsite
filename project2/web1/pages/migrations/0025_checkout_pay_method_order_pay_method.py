# Generated by Django 5.0.1 on 2024-01-12 05:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0024_delete_payment"),
    ]

    operations = [
        migrations.AddField(
            model_name="checkout",
            name="pay_method",
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="pay_method",
            field=models.CharField(max_length=10, null=True),
        ),
    ]
