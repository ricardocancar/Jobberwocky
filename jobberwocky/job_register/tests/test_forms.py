from django.test import TestCase, Client
from django.urls import reverse
from job_register.forms import JobForm


class TestForms(TestCase):
    def test_JobForm_is_valid(self):
        form = JobForm(
            {
                "name": "Python",
                "description": "Python is a programming language",
                "country": "USA",
                "salary_min": 100,
                "salary_max": 200,
                "experience": "1 year",
                "skills": "python, django",
                "currency": "USD",
            }
        )
        self.assertTrue(form.is_valid())

    def test_JobForm_is_no_data(self):
        form = JobForm()
        self.assertFalse(form.is_valid())
