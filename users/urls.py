"""Определение хсемы URL для пользователей"""

from django.urls import path, include

app_name = 'users'
urlpatterns = [
    # Включить URL авторизацию по умолчанию.
    path('', include('django.contrib.auth.urls')),
]