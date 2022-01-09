from django.http import HttpResponse
from django.views import View
from job_register.forms import JobForm
from django.urls import reverse
from django.shortcuts import render, redirect

from job_register.models import Jobs

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


# this will be the search engine function
class GetJobs(View):
    def get(self, request):
        job = Jobs.objects.all()
        ctx = {"jobs_list": job}
        return render(request, "job_register/jobs_list.html", ctx)

