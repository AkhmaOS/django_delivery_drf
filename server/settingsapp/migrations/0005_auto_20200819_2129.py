# Generated by Django 2.2.3 on 2020-08-19 18:29

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('settingsapp', '0004_auto_20200819_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settingsapplication',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='номер телефона'),
        ),
    ]
