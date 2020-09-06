from django.contrib import admin

from .models import SettingsApplication


@admin.register(SettingsApplication)
class SettingsApplicationAdmin(admin.ModelAdmin):
    list_display = ('primary_color', 'second_color', 'logo', 'border_radius', 'phone_number')
    readonly_fields = ('user',)
