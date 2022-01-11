from django import urls
from django.test import SimpleTestCase
from django.urls import resolve, reverse
from job_register.views import Create, Search_v1, Search

class TestUrls(SimpleTestCase):


    def test_create_url_is_resolved(self):
        url = reverse('job_register:create')
        self.assertEquals(resolve(url).func.view_class, Create)
    
    def test_search_v1_url_is_resolved(self):
        url = reverse('job_register:search/v1')
        self.assertEquals(resolve(url).func.view_class, Search_v1)
    def test_search_v2_url_is_resolved(self):
        url = reverse('job_register:search/v2')
        self.assertEquals(resolve(url).func.view_class, Search)