# Generated by Django 2.2.3 on 2020-08-26 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200826_1802'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='name',
        ),
    ]