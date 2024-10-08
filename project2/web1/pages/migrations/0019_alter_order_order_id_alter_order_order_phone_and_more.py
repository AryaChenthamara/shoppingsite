# Generated by Django 4.2.6 on 2023-12-22 04:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0018_alter_order_order_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="order_id",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="order_phone",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="order_pincode",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="order_price",
            field=models.FloatField(null=True),
        ),
    ]
