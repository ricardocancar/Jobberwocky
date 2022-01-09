from django.test import TestCase, Client
from django.urls import reverse
from job_register.models import Jobs

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.create_url = reverse("job_register:create")
        self.search_url = reverse("job_register:search")
        self.job1 = Jobs.objects.create(
            name="Java",
            description="Java is a programming language",
            country="USA",
            salary_min=100,
            salary_max=200,
            experience="1 year",
            skills="java, spring",
            currency="USD",
        )

    def test_create_page(self):
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "job_register/form.html")

    def test_create_page_post(self):
        response = self.client.post(
            self.create_url,
            {
                "name": "Python",
                "description": "Python is a programming language",
                "country": "USA",
                "salary_min": 100,
                "salary_max": 200,
                "experience": "1 year",
                "skills": "python, django",
                "currency": "USD",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("job_register:main"))

    def test_main_page(self):
        response = self.client.get(reverse("job_register:main"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "job_register/main.html")

