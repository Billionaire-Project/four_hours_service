from django.urls import path
from apps.posts import views

urlpatterns = [
    path("", views.post.PostList.as_view(), name="posts"),
    path("<int:pk>/", views.post.PostId.as_view(), name="post"),
    path("my/", views.post_my.PostMy.as_view(), name="post_my"),
]
