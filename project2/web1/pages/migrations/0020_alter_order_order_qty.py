# Generated by Django 4.2.6 on 2023-12-22 04:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0019_alter_order_order_id_alter_order_order_phone_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="order_qty",
            field=models.IntegerField(null=True),
        ),
    ]
