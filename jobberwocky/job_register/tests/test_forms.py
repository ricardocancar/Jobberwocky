from django.test import TestCase, Client
from django.urls import reverse
from job_register.forms import JobForm


class TestForms(TestCase):        
    def test_JobForm_is_valid(self):
        form = JobForm(data={
            'job_name': 'test_job_name',
            'job_description': 'test_job_description',
            'job_country': 'test_job_country',
            'job_salary_min': 100,
            'job_salary_max': 200,
            'job_experience': 'test_job_experience',
            'job_skills': 'test_job_skills',
            'job_currency': 'test_job_currency',
        })

    def test_JobForm_is_no_data(self):
        form = JobForm()
        self.assertFalse(form.is_valid())
