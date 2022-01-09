from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "job_register"
urlpatterns = [
    path("", TemplateView.as_view(template_name="job_register/main.html"), name="main"),
    path("create/", views.Create.as_view(), name="create"),
    path("search/", views.GetJobs.as_view(), name="search"),
]
