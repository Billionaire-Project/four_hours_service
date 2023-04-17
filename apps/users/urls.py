from django.urls import path

from apps.users import views


urlpatterns = [
    path("me/", views.Me.as_view(), name="me"),
]
