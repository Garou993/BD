"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("all_clients/", include("polls.urls.all_clients_urls")),
    path("register/", include ("polls.urls.register_urls")),
    path("login/", include ("polls.urls.login_urls")),
    path("change_password/", include("polls.urls.change_password_urls")),
    path("create_order/", include("polls.urls.create_order")),
    path("logout/", include ("polls.urls.logout_urls")),
    path("profile/", include("polls.urls.profile_urls")),
    path("make_order_service/", include("polls.urls.make_order_service_urls")),    
    path("my_orders/", include("polls.urls.my_orders_urls")),
    path("get_order/", include("polls.urls.get_order")),
    path("delete_order/", include("polls.urls.delete_order")),
    path("leave_master_comment/", include("polls.urls.leave_master_comment_urls")),
    path("leave_item_comment/", include("polls.urls.leave_item_comment_urls")),
    path("tech_supp/", include("polls.urls.tech_supp")),
    path("show_question/", include("polls.urls.show_question")),
    path("leave_comment_courier/", include("polls.urls.leave_comment_courier"))
]