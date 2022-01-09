from django import urls
from django.test import SimpleTestCase
from django.urls import resolve, reverse
from job_register.views import Create, GetJobs

class TestUrls(SimpleTestCase):


    def test_create_url_is_resolved(self):
        url = reverse('job_register:create')
        self.assertEquals(resolve(url).func.view_class, Create)
    
    def test_search_url_is_resolved(self):
        url = reverse('job_register:search')
        self.assertEquals(resolve(url).func.view_class, GetJobs)