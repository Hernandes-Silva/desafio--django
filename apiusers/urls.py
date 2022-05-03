from django.urls import path

from django.urls.conf import include

from apiusers.views import APICreateAdmin, APICreateUser



urlpatterns = [
    path('user-create/', APICreateUser.as_view(), name="user-create"),
    path('admin-create/', APICreateAdmin.as_view(), name="admin-create")
]