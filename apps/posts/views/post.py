import datetime
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema

from apps.commons.views.pagination import Pagination
from apps.posts.serializers import (
    PostGetSerializer,
    PostPostSerializer,
    PostObscuredSerializer,
)
from apps.posts.models import Post, PostObscured


pagination = Pagination(0, 10)


class Posts(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="""
        # receipt확인 후 권한이 있는 유저에게 반환
        ### - 반환은 다음과 같다
        ```
        {
            "start": 0,
            "offset": 10,
            "next": 10,
            "posts": [...],
        }
        ```
        ### - 다음 요청시에는 next값을 start로 요청해주세요!
        ### - next가 null이면 더이상 요청할 데이터가 없습니다.
        ### - 삭제되거나 해당유저에게 신고된 글을 제외하고 반환합니다.
        ### - count_meaningful_words (token)이 5개 이상이라면 핵심단어를 추출 후 obscured
        """,
        manual_parameters=pagination.get_params,
    )
    def get(self, request):
        queryset = Post.objects.filter(is_deleted=False)
        queryset = queryset.filter(
            updated_at__gte=datetime.datetime.now() - datetime.timedelta(days=1)
        )
        queryset = queryset.exclude(post_reports__user_id=request.user.id)
        queryset = queryset.order_by("-updated_at")

        result = pagination.get(request, queryset)
        serializer = PostGetSerializer(
            result.pop("result"),
            many=True,
            context={"request": request},
        )

        result["posts"] = serializer.data

        return Response(result, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="""
        # post를 작성합니다.
        """,
        request_body=PostPostSerializer,
        responses={
            200: PostPostSerializer(),
        },
    )
    def post(self, request, format=None):
        """

        ---
        포스트 작성
        """
        serializer = PostPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
