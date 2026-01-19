from django.urls import path
from .api_views import job_list_create_api

urlpatterns = [
    path('jobs/', job_list_create_api),
]
