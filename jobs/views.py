from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Job

@login_required
def create_job(request):
    if request.user.role != "recruiter":
        return redirect("jobseeker_dashboard")

    if request.method == "POST":
        Job.objects.create(
            title=request.POST.get("title"),
            company=request.POST.get("company"),
            description=request.POST.get("description"),
            created_by=request.user
        )
        return redirect("job_list")

    return render(request, "jobs/job_create.html")


@login_required
def job_list(request):
    jobs = Job.objects.all()
    return render(request, "jobs/job_list.html", {"jobs": jobs})


@login_required
def edit_job(request, id):
    job = get_object_or_404(Job, id=id)

    if request.user.role != "recruiter" or job.created_by != request.user:
        return redirect("job_list")

    if request.method == "POST":
        job.title = request.POST.get("title")
        job.company = request.POST.get("company")
        job.description = request.POST.get("description")
        job.save()
        return redirect("job_list")

    return render(request, "jobs/job_edit.html", {"job": job})


@login_required
def delete_job(request, id):
    job = get_object_or_404(Job, id=id)

    if request.user.role == "recruiter" and job.created_by == request.user:
        job.delete()

    return redirect("job_list")
