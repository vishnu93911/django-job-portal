from django.urls import path
from .views import create_job,job_list,edit_job,delete_job

urlpatterns=[
    path('',job_list,name='job_list'),
    path('create/',create_job,name='create_job'),
    path('edit/<int:id>/',edit_job,name='edit_job'),    
    path('delete/<int:id>/',delete_job,name='delete_job')
]




