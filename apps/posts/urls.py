from django.urls import path
from apps.posts.views import (
    Posts,
    PostLikeId,
    PostsObscured,
    PostId,
    PostMy,
    PostReceiptCheck,
    PostReportId,
)

urlpatterns = [
    path("<int:pk>/", PostId.as_view(), name="post"),
    path("like/<int:pk>/", PostLikeId.as_view(), name="post_like"),
    path("my/", PostMy.as_view(), name="post_my"),
    path("obscured/", PostsObscured.as_view(), name="post_obscureds"),
    path("receipt/", PostReceiptCheck.as_view(), name="post_receipt"),
    path("report/<int:pk>/", PostReportId.as_view(), name="post_report"),
    path("", Posts.as_view(), name="posts"),
]
