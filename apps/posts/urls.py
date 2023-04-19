from django.urls import path
from apps.posts.views import Posts, PostsObscured, PostId, PostMy

urlpatterns = [
    path("", Posts.as_view(), name="posts"),
    path("obscured/", PostsObscured.as_view(), name="post_obscureds"),
    path("<int:pk>/", PostId.as_view(), name="post"),
    path("my/", PostMy.as_view(), name="post_my"),
]
