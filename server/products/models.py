from django.db import models
from filer.fields.image import FilerImageField


class ProductCategory(models.Model):
    name = models.CharField('название категории', max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товара'


class Product(models.Model):
    name = models.CharField('название товара', max_length=256)
    description = models.TextField('описание товара')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductImage(models.Model):
    image = FilerImageField(on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='product')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Фото товара'
