from django.urls import path
from .views import public_api

urlpatterns = [
    path('api/', public_api, name='public_api'),
]
