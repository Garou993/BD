from django.urls import path
from django.urls import include, path

from .. import views

urlpatterns = [
    path("", views.leave_comment_courier, name="leave_comment_courier"),
]