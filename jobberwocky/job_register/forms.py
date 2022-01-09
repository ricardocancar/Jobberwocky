from django import forms
from django.core.exceptions import ValidationError
from django.core import validators



from django.forms import ModelForm
from job_register.models import Jobs

# Create the form class.
class JobForm(ModelForm):
    class Meta:
        model = Jobs
        # fields = ['name', 'breed', 'comments']
        fields = '__all__'


