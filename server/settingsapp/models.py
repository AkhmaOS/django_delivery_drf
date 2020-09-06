from colorfield.fields import ColorField
from django.contrib.auth import get_user_model
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

User = get_user_model()


class SettingsApplication(models.Model):
    user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
    primary_color = ColorField('основной цвет', default='#FF0000')
    second_color = ColorField('вторичный цвет', default='#FF0000')
    logo = models.ImageField('логотип', upload_to='static/img/')
    border_radius = models.IntegerField('закругление')
    phone_number = PhoneNumberField('номер телефона')

    def __str__(self):
        return f'Настройка приложения {self.id}'

    class Meta:
        verbose_name = 'Настройка приложения'
        verbose_name_plural = 'Настройки приложения'
