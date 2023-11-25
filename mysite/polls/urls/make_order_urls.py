from django.urls import path
from django.urls import include, path

from .. import views

urlpatterns = [
    path("", views.make_order_item, name="make_order_item"),
]