from django.utils import timezone

from rest_framework import status
from rest_framework import exceptions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema

# from drf_yasg import openapi

from apps.posts.serializers import PostGetSerializer
from apps.posts.models import Post


class PostId(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            post = Post.objects.get(id=pk)
            return post
        except post.DoesNotExist:
            raise exceptions.NotFound

    @swagger_auto_schema(
        operation_description="post를 가져옵니다.",
        responses={
            200: PostGetSerializer(),
        },
    )
    def get(self, request, pk, format=None):
        # 여기에 is_delete가 true인애 면 404
        post = self.get_object(pk)
        serializer = PostGetSerializer(post, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="post를 삭제합니다. (soft delete)",
    )
    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.is_deleted = True
        post.deleted_at = timezone.now()
        post.save()
        return Response(status=status.HTTP_200_OK)
