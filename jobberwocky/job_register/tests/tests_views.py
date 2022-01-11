from django.test import TestCase, Client
from django.urls import reverse
from job_register.models import Jobs, Skills, Company

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.create_url = reverse("job_register:create")
        self.search_url = reverse("job_register:search/v1")
        self.skill_1 = Skills(
            name='python'
        )
        self.skill_1.save()

        self.company = Company(
            company_name='Google',
            company_email='google@mail.com',
            company_description='Google is a company',
            company_website='https://www.google.com',
            company_address='Google address',
            company_country='US',
            company_phone='+11234567890'
        )
        self.company.save()
        self.job_1 = Jobs(
            company=self.company,
            job_name='Python Developer',
            description='Python developer',
            country='US',
            salary_min=100,
            salary_max=200,
            experience='1 years',
            currency='USD',
        )
        self.job_1.save()
        self.job_1.skills.add(self.skill_1
    )
    def test_create_page(self):
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "job_register/form.html")

    def test_create_page_post(self):
        # create a job with skills
        response = self.client.post(self.create_url, {
            'job_name': 'test_job_name',
            'description': 'test_job_description',
            'country': 'US',
            'salary_min': 100,
            'salary_max': 200,
            'experience': '3 years',
            'skills': '1',
            'currency': 'GBP',
            'company': '1',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Jobs.objects.count(), 2)

    def test_main_page(self):
        response = self.client.get(reverse("job_register:main"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "job_register/main.html")

