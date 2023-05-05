from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema

from apps.commons.views.pagination import Pagination
from apps.posts.serializers import PostObscuredSerializer
from apps.posts.models import PostObscured

pagination = Pagination(0, 10)


class PostsObscured(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="""
        ## receipt확인 후 권한이 없는 유저에게 반환
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
        """,
        manual_parameters=pagination.get_params,
        responses={
            200: PostObscuredSerializer(many=True),
        },
    )
    def get(self, request, format=None):
        queryset = PostObscured.objects.filter(is_deleted=False).order_by("-created_at")
        result = pagination.get(request, queryset)
        serializer = PostObscuredSerializer(
            result.pop("result"),
            many=True,
        )

        result["posts"] = serializer.data

        return Response(result)
