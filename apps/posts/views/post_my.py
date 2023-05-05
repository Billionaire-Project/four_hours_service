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
        operation_description="""
        내가 작성한 post를 가져옵니다.
         - 반환은 다음과 같다
        ```
        {
            "start": 0,
            "offset": 10,
            "next": 10,
            "posts": [...],
        }
        ```
        - 다음 요청시에는 next값을 start로 요청해주세요!
        - next가 null이면 더이상 요청할 데이터가 없습니다.
        """,
        manual_parameters=pagination.get_params,
        responses={
            200: PostMySerializer(many=True),
        },
    )
    def get(self, request, format=None):
        queryset = Post.objects.filter(is_deleted=False, user=request.user).order_by(
            "-created_at"
        )
        result = pagination.get(request, queryset)
        serializer = PostMySerializer(
            result.pop("result"),
            many=True,
        )
        result["posts"] = serializer.data
        return Response(result)
