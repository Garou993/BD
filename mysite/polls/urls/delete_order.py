from django.urls import path
from django.urls import include, path

from .. import views

urlpatterns = [
    path("", views.delete_order, name="delete_order"),
]