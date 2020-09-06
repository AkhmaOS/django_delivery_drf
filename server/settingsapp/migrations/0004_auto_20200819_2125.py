# Generated by Django 2.2.3 on 2020-08-19 18:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('settingsapp', '0003_auto_20200811_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='settingsapplication',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='settingsapplication',
            name='border_radius',
            field=models.IntegerField(verbose_name='закругление'),
        ),
        migrations.AlterField(
            model_name='settingsapplication',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]