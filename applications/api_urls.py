from django.urls import path
from .api_views import apply_job_api

urlpatterns = [
    path('apply/<int:job_id>/', apply_job_api),
]
