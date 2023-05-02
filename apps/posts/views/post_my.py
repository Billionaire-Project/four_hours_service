from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from apps.commons.views.pagination import Pagination

from apps.posts.serializers import PostMySerializer
from apps.posts.models import Post

pagination = Pagination(0, 10)


class PostMy(APIView):
    @swagger_auto_schema(
        operation_description="내가 작성한 post를 가져옵니다.",
        manual_parameters=pagination.get_params,
        responses={
            200: PostMySerializer(many=True),
        },
    )
    def get(self, request, format=None):
        queryset = Post.objects.filter(is_deleted=False).filter(user=request.user)
        my_posts = pagination.get(request, queryset)
        serializer = PostMySerializer(my_posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
