from django.urls import path
from apps.posts.views import Posts, PostsObscured, PostId, PostMy, PostReceiptCheck

urlpatterns = [
    path("", Posts.as_view(), name="posts"),
    path("my/", PostMy.as_view(), name="post_my"),
    path("receipt/", PostReceiptCheck.as_view(), name="post_receipt"),
    path("obscured/", PostsObscured.as_view(), name="post_obscureds"),
    path("<int:pk>/", PostId.as_view(), name="post"),
]
