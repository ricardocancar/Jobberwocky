from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinLengthValidator

COUNTRIES = [
    ("United States", "United States"),
    ("Spain", "Spain"),
    ("United Kingdom", "United Kingdom"),
]
CURRENCY = [("USD", "USD"), ("EUR", "EUR"), ("GBP", "GBP")]
EXPERIENCE = [
    ("1 years", "1 years"),
    ("2 years", "2 years"),
    ("3 years", "3 years"),
    ("4 years", "4 years"),
    ("5 years", "5 years"),
]


class Skills(models.Model):
    """
    skills many to many relationship with jobs
    """

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Company(models.Model):
    """
    Company model to store the data in the database wih the following fields
    """

    company_name = models.CharField(max_length=100)
    company_email = models.EmailField()
    # password = models.CharField(max_length=100)
    company_description = models.CharField(max_length=500)
    company_website = models.URLField()
    company_address = models.CharField(max_length=100)
    company_country = models.CharField(max_length=50, choices=COUNTRIES)
    company_phone = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name



class Jobs(models.Model):
    """
    Jobs model to store the data in the database wih the following fields
    """

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True, blank=True)
    country = models.CharField(max_length=50, choices=COUNTRIES)
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    experience = models.CharField(max_length=100, choices=EXPERIENCE)
    skills = models.ManyToManyField(Skills)
    currency = models.CharField(max_length=3, choices=CURRENCY)
    # add one field to create a foreign key to the Employer model

    def __str__(self):
        return self.job_name


# create an user model with name, email, password, user type (employer or candidate) and profession
# profession is a foreign key to the Jobs model
class User(models.Model):
    """
    user model to store the data in the database wih the following fields
    allowing the applications sending  the candidates an email alert
    """
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    def __str__(self):
        return self.name
