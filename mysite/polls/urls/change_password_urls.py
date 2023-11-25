from django.urls import path
from django.urls import include, path

from .. import views

urlpatterns = [
    path("", views.change_password, name="change_password"),
]