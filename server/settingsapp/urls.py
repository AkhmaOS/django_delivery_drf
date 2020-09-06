from django.urls import path

from .views import SettingsApplicationView


urlpatterns = [
    path('settings/', SettingsApplicationView.as_view(), name='settings-app'),
]
