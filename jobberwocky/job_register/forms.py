from django import forms
from django.core.exceptions import ValidationError
from django.core import validators


from django.forms import ModelForm
from job_register.models import Jobs


class JobForm(ModelForm):
    class Meta:
        model = Jobs
        fields = "__all__"
