from django.urls import path

from apps.users import views


urlpatterns = [
    path("test/", views.UserTest.as_view(), name="user_test"),
]
