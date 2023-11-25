from django.urls import path
from django.urls import include, path

from .. import views

urlpatterns = [
    path("", views.make_orders_service, name="make_order_service"),
]