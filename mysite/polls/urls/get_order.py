from django.urls import path
from django.urls import include, path

from .. import views

urlpatterns = [
    path("", views.get_order, name="get_order"),
]