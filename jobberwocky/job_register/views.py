from django.views import View
from job_register.forms import JobForm
from django.urls import reverse
from django.shortcuts import render, redirect

from job_register.models import Jobs
from job_register import get_externals_job_offers
import requests

# Create your views here.

# exercise part 1
class Create(View):
    def get(self, request):
        form = JobForm()
        ctx = {"form": form}
        return render(request, "job_register/form.html", ctx)

    def post(self, request):
        form = JobForm(request.POST)
        if not form.is_valid():
            ctx = {"form": form}
            return render(request, "job_register/form.html", ctx)

        # Save the form and get a model object
        newjob = form.save()
        x = reverse("job_register:main")
        return redirect(x)


# exercise part 2
class Search_v1(View):
    def get(self, request):
        """
        query the database and return a list of jobs that match the search job_name
        """
        job_name = request.GET.get("job_name", "")
        jobs = Jobs.objects.filter(job_name__contains=job_name)
        # get the the skills for each job
        ctx = {"jobs": jobs}
        return render(request, "job_register/search.html", ctx)


# exercise part 3
class Search(View):
    def get(self, request):
        """
        query the database and externals API to
        return a list of jobs that match the search job_name
        """
        job_name = request.GET.get("job_name", "")
        externals_jobs_offers = get_externals_job_offers(job_name)
        jobs = Jobs.objects.filter(job_name__contains=job_name)
        # get the the skills for each job

        ctx = {"jobs": jobs, "externals_jobs_offers": externals_jobs_offers}
        return render(request, "job_register/search.html", ctx)

