from django.urls import path
from django.urls import include, path

from .. import views

urlpatterns = [
    path("", views.leave_master_comment, name="leave_master_comment"),
]