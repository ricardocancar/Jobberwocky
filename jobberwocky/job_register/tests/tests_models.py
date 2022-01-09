from django.test import TestCase, Client
from django.urls import reverse
from job_register.models import Jobs


class TestModels(TestCase):
    def setUp(self):
        Jobs.objects.create(
            name="Python",
            description="Python is a programming language",
            country="USA",
            salary_min=100,
            salary_max=200,
            experience="1 year",
            skills="python, django",
            currency="USD",
        )
        Jobs.objects.create(
            name="Java",
            description="Java is a programming language",
            country="USA",
            salary_min=100,
            salary_max=200,
            experience="1 year",
            skills="java, spring",
            currency="USD",
        )

    def test_jobs(self):
        """Animals that can speak are correctly identified"""
        python = Jobs.objects.get(name="Python")
        java = Jobs.objects.get(name="Java")
        self.assertEqual(python.name, "Python")
        self.assertEqual(java.name, "Java")

