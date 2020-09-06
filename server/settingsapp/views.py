from rest_framework import generics

from .models import SettingsApplication
from .serializers import SettingsApplicationSerializer


class SettingsApplicationView(generics.ListAPIView):
    queryset = SettingsApplication.objects.all()
    serializer_class = SettingsApplicationSerializer
