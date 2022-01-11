from django.http import HttpResponse
from django.views import View
from job_register.forms import JobForm
from django.urls import reverse
from django.shortcuts import render, redirect

from job_register.models import Jobs, Skills
import requests
# Create your views here.
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


# query the database and return a list of jobs that match the search job_name
class Search(View):
    def get(self, request):
        # call another api to more job list using the following url http://localhost:8081/jobs?name=
        
        job_name = request.GET.get("job_name", '')
        jobs = Jobs.objects.filter(job_name__contains=job_name)
        # get the the skills for each job
        skills = Skills.objects.all()
        ctx = {"jobs": jobs, "skills": skills}
        return render(request, "job_register/search.html", ctx)

# class Search_v2(View):
#     def get(self, request):
#         # call another api to more job list using the following url http://localhost:8081/jobs?name=
        
#         job_name = request.GET.get("job_name", '')
#         response = requests.get(f"http://localhost:8081/jobs?name={job_name}")
#         other_jobs = []
#         if response.status_code  == 200:
#             other_jobs = response.json()
#         { '' for job in other_jobs}
#         jobs = Jobs.objects.filter(job_name__contains=job_name)
#         # get the the skills for each job
#         skills = Skills.objects.all()

        ctx = {"jobs": jobs, "skills": skills}
        return render(request, "job_register/search.html", ctx)

