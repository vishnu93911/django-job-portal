from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Application
from jobs.models import Job
from .serializers import ApplicationSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def apply_job_api(request, job_id):
    if request.user.role != "jobseeker":
        return Response({"error": "Only jobseekers"}, status=403)

    job = Job.objects.get(id=job_id)
    app, created = Application.objects.get_or_create(
        job=job,
        applicant=request.user
    )
    serializer = ApplicationSerializer(app)
    return Response(serializer.data)
