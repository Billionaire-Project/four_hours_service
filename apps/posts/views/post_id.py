from django.utils import timezone

from rest_framework import status
from rest_framework import exceptions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# from drf_yasg import openapi

from apps.posts.serializers import PostGetSerializer
from apps.posts.models import Post, PostDeleteReason


class PostId(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            post = Post.objects.get(id=pk)
            return post
        except post.DoesNotExist:
            raise exceptions.NotFound

    @swagger_auto_schema(
        operation_description="""
        # post를 가져옵니다.
        ### - 요청한 포스트가 삭제되었다면 404를 반환합니다.
        """,
        responses={
            200: PostGetSerializer(),
        },
    )
    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        if post.is_deleted:
            raise exceptions.NotFound

        serializer = PostGetSerializer(
            post,
            context={"request": request},
        )

        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="""
        # post를 삭제합니다.
        ## soft delete
        ### - 요청한 포스트가 삭제되었다면 404를 반환합니다.
        """,
        manual_parameters=[
            openapi.Parameter(
                "reason",
                openapi.IN_QUERY,
                description="삭제 이유의 id",
                type=openapi.TYPE_INTEGER,
                default=1,
            ),
        ],
    )
    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post_delete_reason = request.query_params.get("reason", 1)
        if post.is_deleted:
            raise exceptions.NotFound
        post.delete_reason = PostDeleteReason.objects.get(id=post_delete_reason)
        post.is_deleted = True
        post.deleted_at = timezone.now()
        post.save()
        return Response(status=status.HTTP_200_OK)
