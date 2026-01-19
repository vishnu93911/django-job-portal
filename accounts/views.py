from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User
from jobs.models import Job
from applications.models import Application
from django.conf import settings
# from rest_framework.decorators import api_view
# Create your views here.

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")   
        email = request.POST.get("email")
        role = request.POST.get("role")
        recruiter_code = request.POST.get("recruiter_code")

        if role == "recruiter":
            if recruiter_code != settings.RECRUITER_SECRET_CODE:
                messages.error(request, "Invalid recruiter secret code")
                return redirect("register")

        if not role:
            messages.error(request, "Please select a role")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register")

        user = User.objects.create_user(
            username=username,
            password=password,
            
            email=email
        )
        user.first_name = first_name
        user.last_name = last_name
        user.role = role
        user.save()

        messages.success(request, "Registration successful, please login.")
        return redirect("login")

    return render(request, "accounts/register.html")



def login_view(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_superuser:
                return redirect("/admin/")
            if user.role=="recruiter":
                return redirect("recruiter_dashboard")
            return redirect("jobseeker_dashboard")
        
        messages.error(request,"Invalid username or password")
        
    return render(request,"accounts/login.html")

def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def recruiter_dashboard(request):
    if request.user.is_superuser:
        return redirect("/admin/")
    if request.user.role!="recruiter":
        return redirect("jobseeker_dashboard")
    recruiter_jobs = Job.objects.filter(recruiter=request.user)

    
    applications = Application.objects.filter(job__in=recruiter_jobs)

    context = {
        'jobs': recruiter_jobs,
        'applications': applications,
    }
    return render(request,"accounts/recruiter_dashboard.html",context)

@login_required
def jobseeker_dashboard(request):
    if request.user.is_superuser:
        return redirect("/admin/")
    if request.user.role!="jobseeker":
        return redirect("recruiter_dashboard")
    return render(request,"accounts/jobseeker_dashboard.html")



