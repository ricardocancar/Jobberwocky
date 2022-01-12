from django import forms
from django.core.exceptions import ValidationError
from django.core import validators


from django.forms import ModelForm
from job_register.models import Jobs, User


class JobForm(ModelForm):
    class Meta:
        model = Jobs
        fields = "__all__"

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = "__all__"


# send a email to the user
# def send_email(self, job_id):
#     job = Jobs.objects.get(id=job_id)
#     subject = "New job offer"
#     message = "Hello, you have a new job offer: " + job.job_name
#     from_email = settings.EMAIL_HOST_USER
#     to_email = [job.job_email]
#     send_mail(subject, message, from_email, to_email, fail_silently=True)
#     return True

