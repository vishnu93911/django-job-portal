from django.urls import path
from .api_views import register_api

urlpatterns = [
    path('register/', register_api),
]
