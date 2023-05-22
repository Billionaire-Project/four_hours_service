from rest_framework import status
from rest_framework import exceptions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema

from apps.commons.views.pagination import Pagination
from apps.posts.models import Post, PostLike
from apps.posts.serializers.post import PostGetSerializer

pagination = Pagination(0, 10)


class PostLikes(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="""
        # 내가 좋아요한 post 목록을 가져옵니다.
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
        """,
        manual_parameters=pagination.get_params,
    )
    def get(self, request, format=None):
        post_like_list = PostLike.objects.filter(
            user=request.user,
        ).values_list(
            "post_id",
            flat=True,
        )

        queryset = Post.objects.filter(is_deleted=False)
        queryset = queryset.exclude(post_reports__user_id=request.user.id)
        queryset = queryset.filter(id__in=post_like_list)
        queryset = queryset.order_by("-created_at")

        result = pagination.get(request, queryset)
        serializer = PostGetSerializer(
            result.pop("result"),
            many=True,
            context={"request": request},
        )

        result["posts"] = serializer.data
        return Response(result, status=status.HTTP_200_OK)
