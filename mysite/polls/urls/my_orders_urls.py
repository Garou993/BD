from django.urls import path
from django.urls import include, path

from .. import views

urlpatterns = [
    path("", views.my_orders, name="my_orders"),
]