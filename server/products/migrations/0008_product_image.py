# Generated by Django 2.2.3 on 2020-08-26 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_remove_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ManyToManyField(related_name='product_image', to='products.ProductImage'),
        ),
    ]
