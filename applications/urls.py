from django.urls import path

from .views import apply_job,view_applications,view_jobs
from . import views
urlpatterns=[
    path('apply/<int:job_id>/',apply_job,name='apply_job'),
    path('view/',view_applications,name='view_applications'),
    path('jobs/', view_jobs, name='view_jobs'), 
    path("shortlist/<int:pk>/", views.shortlist_application, name="shortlist"),
    path("reject/<int:pk>/", views.reject_application, name="reject"),
]


