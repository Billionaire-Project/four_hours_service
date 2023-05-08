from rest_framework import status
from rest_framework import exceptions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema

from apps.posts.models import Post, PostLike


class PostLikeId(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            post = Post.objects.get(id=pk)
            return post
        except post.DoesNotExist:
            raise exceptions.NotFound

    @swagger_auto_schema(
        operation_description="""
        ## post를 좋아요합니다.
        - post_id를 path parameter로 받습니다.
        - 해당 api를 다시 요청하면 좋아요가 취소됩니다.
        """,
    )
    def post(self, request, pk, format=None):
        post = self.get_object(pk)

        post_like, created = PostLike.objects.get_or_create(
            user=request.user,
            post=post,
        )

        if not created:
            post_like.delete()

        return Response(status=status.HTTP_200_OK)
