from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from apps.posts.serializers import PostMySerializer
from apps.posts.models import Post


class PostMy(APIView):
    @swagger_auto_schema(
        operation_description="내가 작성한 post를 가져옵니다.",
        responses={
            200: PostMySerializer(many=True),
        },
    )
    def get(self, request, format=None):
        my_posts = Post.objects.filter(is_deleted=False).filter(user=request.user)
        if not my_posts:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = PostMySerializer(my_posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
