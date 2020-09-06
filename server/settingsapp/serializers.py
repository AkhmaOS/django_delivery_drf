from rest_framework import serializers

from .models import SettingsApplication


class SettingsApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SettingsApplication
        fields = ('primary_color', 'second_color', 'logo', 'border_radius', 'phone_number')
