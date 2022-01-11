from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinLengthValidator

# create a job model to store the data in the database wih the following fields
# name, description, country, salary_min, salary_max,
#  experience, skills, qualifications
class Skills(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# create a employer model to store the data in the database wih the following fields
# name, email, password, company_name, company_description, company_website, company_address, company_country,  company_phone
class Company(models.Model):
    company_name = models.CharField(max_length=100)
    company_email = models.EmailField()
    # password = models.CharField(max_length=100)
    company_description = models.CharField(max_length=500)
    company_website = models.URLField()
    company_address = models.CharField(max_length=100)
    company_country = models.CharField(
        max_length=2,
        choices=[("US", "United States"), ("ES", "Spain"), ("UK", "United Kingdom")],
    )
    company_phone = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name


class Jobs(models.Model):
    COUNTRIES = [("US", "United States"), ("ES", "Spain"), ("UK", "United Kingdom")]
    CURRENCY = [("USD", "USD"), ("EUR", "EUR"), ("GBP", "GBP")]
    EXPERIENCE = [("1 years", "1 years"), ("2 years", "2 yearss"), ("3 years", "3 years"), ("4 years", "4 years"), ("5 years", "5 years")]
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True, blank=True)
    country = models.CharField(max_length=2, choices=COUNTRIES)
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    experience = models.CharField(max_length=100, choices=EXPERIENCE)
    skills = models.ManyToManyField(Skills)
    currency = models.CharField(max_length=3, choices=CURRENCY)
    # add one field to create a foreign key to the Employer model

    def __str__(self):
        return self.job_name


# # create an user model with name, email, password, user type (employer or candidate) and profession
# # profession is a foreign key to the Jobs model
# class User(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)
#     password = models.CharField(max_length=100)
#     user_type = models.CharField(max_length=10, choices=[('employer', 'employer'), ('candidate', 'candidate')])
#     profession = models.ForeignKey(Jobs, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.name
