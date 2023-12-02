from django.urls import path
from django.urls import include, path

from .. import views

urlpatterns = [
    path("", views.leave_item_comment, name="leave_item_comment"),
]