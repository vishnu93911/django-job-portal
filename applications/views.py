from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from django.http import JsonResponse
from .models import Application
from jobs.models import Job


@login_required
def view_jobs(request):
    if request.user.role != "jobseeker":
        return redirect("view_applications")

    jobs = Job.objects.all()
    return render(request, "applications/view_jobs.html", {"jobs": jobs})


@login_required
def apply_job(request, job_id):
    if request.user.role != "jobseeker":
        return JsonResponse(
            {"error": "You are not allowed to apply"},
            status=403
        )

    job = get_object_or_404(Job, id=job_id)

    application, created = Application.objects.get_or_create(
        job=job,
        applicant=request.user
    )

    if created:
        return JsonResponse({
            "message": "✅ Successfully applied for the job! We will review and email you soon."
        })
    else:
        return JsonResponse({
            "message": "⚠️ You have already applied for this job."
        })

# @login_required
# def view_applications(request):
#     if request.user.role != "recruiter":
#         return redirect("jobseeker_dashboard")

#     # Filter applications for jobs posted by this recruiter
#     applications = Application.objects.filter(
#         job__recruiter=request.user
#     ).select_related('job', 'applicant')
 
#     return render(
#         request,
#         "applications/application_list.html",
#         {"applications": applications}
#     )
@login_required
def view_applications(request):
    if request.user.is_superuser:
        return redirect("/admin/")

    if request.user.role != "recruiter":
        return redirect("jobseeker_dashboard")

    applications = Application.objects.all()

    return render(
        request,
        "applications/application_list.html",
        {"applications": applications}
    )

@login_required
@require_POST
def shortlist_application(request, pk):
    if request.user.role != "recruiter":
        return JsonResponse({"error": "Unauthorized"}, status=403)

    app = Application.objects.get(id=pk)
    app.status = "shortlisted"
    app.save()
    return JsonResponse({"success": True})


@login_required
@require_POST
def reject_application(request, pk):
    if request.user.role != "recruiter":
        return JsonResponse({"error": "Unauthorized"}, status=403)
    app = Application.objects.get(id=pk)
    app.delete()
    return JsonResponse({"success": True})

 
# @login_required
# def recruiter_dashboard(request):
#     if request.user.role != "recruiter":
#         return redirect("jobseeker_dashboard")

#     jobs = Job.objects.filter(recruiter=request.user)
#     return render(request, "applications/recruiter_dashboard.html", {"jobs": jobs})

# # AJAX: Get Applicants for a Job
# @login_required
# def get_applicants(request, job_id):
#     if request.user.role != "recruiter":
#         return JsonResponse({"error": "Not allowed"}, status=403)

#     job = get_object_or_404(Job, id=job_id, recruiter=request.user)
#     applications = Application.objects.filter(job=job).select_related('applicant')

#     applicants_data = [
#         {
#             "username": app.applicant.username,
#             "email": app.applicant.email,
#             "applied_at": app.applied_at.strftime("%d %b %Y %H:%M")
#         }
#         for app in applications
#     ]

#     return JsonResponse({"applicants": applicants_data})