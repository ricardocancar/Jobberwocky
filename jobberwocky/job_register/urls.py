from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "job_register"
urlpatterns = [
    path("", TemplateView.as_view(template_name="job_register/main.html"), name="main"),
    path("create/", views.Create.as_view(), name="create"),
    path(
        "search/engine/v1/",
        TemplateView.as_view(template_name="job_register/search_engine.html"),
        name="search/engine/v1",
    ),
    path(
        "search/engine/v2/",
        TemplateView.as_view(template_name="job_register/search_engine_v2.html"),
        name="search/engine/v2",
    ),
    path("search/v1/", views.Search.as_view(), name="search/v1"),
    path("search/v2/", views.Search.as_view(), name="search/v2"),
    path("signin/", views.SignIn.as_view(), name="signin"),
]
