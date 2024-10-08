# Generated by Django 4.2.4 on 2024-02-03 05:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0025_checkout_pay_method_order_pay_method"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="pro_user",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="checkout",
            name="pro_user",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="pro_user",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="wishlist",
            name="pro_user",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
