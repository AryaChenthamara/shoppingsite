# Generated by Django 4.2.5 on 2023-11-04 05:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0009_rename_pro_img_category_cat_img_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="pro_cat",
            field=models.IntegerField(null=True),
        ),
    ]
