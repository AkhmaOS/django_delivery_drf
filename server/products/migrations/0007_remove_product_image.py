# Generated by Django 2.2.3 on 2020-08-26 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
