from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Job


def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs': jobs})


def detail(request, job_id):
    detailjob = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/jobdetail.html', {'detailjob': detailjob})
