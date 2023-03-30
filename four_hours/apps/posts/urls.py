from django.urls import path
from apps.posts.views import post

urlpatterns = [
    path("", post.PostList.as_view(), name="posts"),
]
