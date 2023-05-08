from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from django.utils import timezone
from firebase_admin import auth
from apps.commons.views.pagination import Pagination
from apps.posts.serializers.post_my import PostMySerializer
from apps.posts.serializers.post_receipt import PostReceiptSerializer

from apps.users.models import User
from apps.users.models import UserSession
from apps.users.serializers.serializers import UserSerializer
from apps.posts.models import Post, PostReceipt
from apps.posts.serializers import PostGetSerializer, PostPostSerializer


pagination = Pagination(0, 10)


class Test(APIView):
    """
    # api test용
    - 단순 테스트용입니다. 신경쓰지 마세요.
    """

    @swagger_auto_schema(
        operation_description="""
        ## receipt확인 후 권한이 있는 유저에게 반환
        - 반환은 다음과 같다
        ```
        {
            "start_from": 0,
            "offset": 10,
            "posts": [...],
            "status": 200
        }
        ```
        - 다음 요청시에는 start_from에 offset을 더한 값으로 요청해주세요
        """,
        # manual_parameters=page.get_params,
        responses={
            200: PostGetSerializer(many=True),
        },
    )
    def get(self, request):
        queryset = Post.objects.filter(is_deleted=False, user=request.user).order_by(
            "-created_at"
        )
        result = pagination.get(request, queryset)
        serializer = PostMySerializer(
            result.pop("result"),
            many=True,
        )
        # serializer.data의 인자를 날짜별로 묶어서 반환
        posts_by_date = {}
        for post in serializer.data:
            if post["created_at"][:10] not in posts_by_date:
                posts_by_date[post["created_at"][:10]] = [post]
            else:
                posts_by_date[post["created_at"][:10]].append(post)

        result["posts"] = posts_by_date

        # print(request.user.post_reports.all())

        return Response(result)

        # 여기서는 단순 확인기능만, PostReceipt 관련 테스트
        # post_receipt = PostReceipt.objects.get(user_id=request.user.id)
        # serializer = PostReceiptSerializer(post_receipt)

        # return Response(serializer.data)
