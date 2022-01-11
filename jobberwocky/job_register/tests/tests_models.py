from collections import namedtuple
from django.test import TestCase, Client
from django.urls import reverse
from job_register.models import Jobs, Skills, Company


class TestModels(TestCase):
    def setUp(self):
        # add some skills to models
        self.skill_1 = Skills(
            name='python'
        )
        self.skill_1.save()
        self.skill_2 = Skills(
            name='django'
        )
        self.skill_2.save()
        self.skill_3 = Skills(
            name='java'
        )
        self.skill_3.save()
        self.skill_4 = Skills(
            name='spring'
        )
        self.skill_4.save()
        # create some Company to models
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
        self.job_1.skills.add(self.skill_1, self.skill_2)
        
        self.job_2 = Jobs(
            job_name='java developer',
            description='java developer',
            country='US',
            salary_min=100,
            salary_max=200,
            experience='1 years',
            currency='USD',
            company=self.company
        )
        self.job_2.save()
        self.job_2.skills.add(self.skill_3, self.skill_4)


    def test_jobs(self):
        """ """
        python = Jobs.objects.get(job_name="Python Developer")
        java = Jobs.objects.get(job_name="java developer")
        self.assertEqual(python.job_name, "Python Developer")
        self.assertEqual(java.job_name, "java developer")

    def test_skills_in_jobs(self):
        """ """
        python = Jobs.objects.get(job_name="Python Developer")
        java = Jobs.objects.get(job_name="java developer")
        self.assertEqual(python.skills.all()[0].name, "python")
        self.assertEqual(java.skills.all()[0].name, "java")
        self.assertEqual(python.skills.all()[1].name, "django")
        self.assertEqual(java.skills.all()[1].name, "spring")

    def test_company_in_jobs(self):
        """ """
        python = Jobs.objects.get(job_name="Python Developer")
        java = Jobs.objects.get(job_name="java developer")
        self.assertEqual(python.company.company_name, "Google")
        self.assertEqual(java.company.company_name, "Google")