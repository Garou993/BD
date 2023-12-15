from django.urls import path
from django.urls import include, path

from .. import views

urlpatterns = [
    path("", views.tech_supp, name="tech_supp"),
]