from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinLengthValidator

# create a job model to store the data in the database wih the following fields
# name, description, country, salary_min, salary_max,
#  experience, skills, qualifications

class Jobs(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    country = models.CharField(max_length=100)
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    experience = models.CharField(max_length=100)
    skills = models.CharField(max_length=500)
    currency = models.CharField(max_length=3)
    def __str__(self):
        return self.name
