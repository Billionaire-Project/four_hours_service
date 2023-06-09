from django.urls import path
from apps.posts.views import (
    Posts,
    PostLikeId,
    PostLikes,
    PostsObscured,
    PostId,
    PostMy,
    PostReceiptCheck,
    PostReportId,
    PostDeleteReasons,
)

urlpatterns = [
    path("<int:pk>/", PostId.as_view(), name="post"),
    path("like/<int:pk>/", PostLikeId.as_view(), name="post_like_id"),
    path("likes/", PostLikes.as_view(), name="post_likes"),
    path("my/", PostMy.as_view(), name="post_my"),
    path("obscured/", PostsObscured.as_view(), name="post_obscureds"),
    path("receipt/", PostReceiptCheck.as_view(), name="post_receipt"),
    path("report/<int:pk>/", PostReportId.as_view(), name="post_report"),
    path("delete_reason/", PostDeleteReasons.as_view(), name="post_delete_reason"),
    path("", Posts.as_view(), name="posts"),
]
