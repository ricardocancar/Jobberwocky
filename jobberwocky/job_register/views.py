from django.views import View
from job_register.forms import JobForm, UserForm
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404

from job_register.models import Jobs, User
from job_register import get_externals_job_offers, smtp
from job_register.send_email import send_email

# exercise part 1
class Create(View):
    """
    class to create a new job offer
    """
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
        # part 4

        users = User.objects.filter(profession__contains=newjob.job_name)
        if users:
            for user in users:
                send_email(smtp, user, newjob)
        x = reverse("job_register:main")
        return redirect(x)


class SignIn(View):
    """
    allow job seeker to sign in to receive job offers by email
    """
    def get(self, request):
        form = UserForm()
        ctx = {"form": form}
        return render(request, "job_register/form.html", ctx)

    def post(self, request):
        form = UserForm(request.POST)
        if not form.is_valid():
            ctx = {"form": form}
            return render(request, "job_register/form.html", ctx)

        # Save the form and get a model object
        newuser = form.save()
        x = reverse("job_register:main")
        return redirect(x)


# exercise part 2


class Search_v1(View):
    def get(self, request, job_name=""):
        """
        query the database and return a list of jobs that match the search job_name
        """
        # filter jobs by job_name
        jobs = Jobs.objects.filter(job_name__contains=job_name)
        # get the the skills for each job
        ctx = {"jobs": jobs}
        return render(request, "job_register/search.html", ctx)


# exercise part 3
class Search_v2(View):
    def get(self, request, job_name=""):
        """
        query the database and externals API to
        return a list of jobs that match the search job_name
        """
        # filter jobs by job_name
        jobs = Jobs.objects.filter(job_name__contains=job_name)
        # get the the skills for each job
        externals_jobs_offers = get_externals_job_offers(job_name)

        ctx = {"jobs": jobs, "externals_jobs_offers": externals_jobs_offers}
        return render(request, "job_register/search.html", ctx)

