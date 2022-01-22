from django.views import View
from job_register.forms import JobForm, UserForm
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404

from job_register.models import Jobs, User
from job_register import get_externals_job_offers, smtp
from job_register.send_email import SendEmail

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
                send_email = SendEmail(user, newjob)
                send_email.email_sender(smtp)
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

class Search(View):
    # serch internals jobs
    def search_internal_data(self):
        self.job_name = self.request.GET.get("job_name", '')
        self.jobs = Jobs.objects.filter(job_name__contains=self.job_name)
        return self.jobs

    
    def search_externals_data(self):
        """ query the database and externals API to"""
        self.externals_jobs_offers = get_externals_job_offers(self.job_name)
        return self.externals_jobs_offers

    # exercise part 2
    def v1(self):
        """
        query the database and return a list of jobs that match the search job_name
        args:
            job_name: string to search for the available jobs
        """
        # filter jobs by job_name
        # get the the skills for each job
        ctx = {"jobs": self.search_internal_data()}
        return render(self.request, "job_register/search.html", ctx)
        # test if jobs match with render the template

    # search externals jobs
    # exercise part 3
    def v2(self):
        """
        query the database and externals API to
        return a list of jobs that match the search job_name
        args:
            job_name: string to search for the available jobs
        """
        # filter jobs by job_name
        # get the the skills for each j

        ctx = {
            "jobs": self.search_internal_data,
            "externals_jobs_offers": self.search_externals_data}
        return render(self.request, "job_register/search.html", ctx)


    def get(self, request):
        self.request = request
        if 'v1' in request.path:
            return self.v1()
        elif 'v2' in request.path:
            return self.v2()
        
    

