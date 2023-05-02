from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from django.utils import timezone
from firebase_admin import auth
from apps.commons.views.pagination import Pagination

from apps.users.models import User
from apps.users.models import UserSession
from apps.users.serializers.serializers import UserSerializer
from apps.posts.models import Post
from apps.posts.serializers import PostGetSerializer, PostPostSerializer


page = Pagination(0, 10)


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
        manual_parameters=page.get_params,
        responses={
            200: PostGetSerializer(many=True),
        },
    )
    def get(self, request):
        queryset = Post.objects.all().order_by("-created_at")
        posts = page.get(request, queryset)
        serializer = PostGetSerializer(
            posts,
            many=True,
            context={"request": request},
        )

        return Response(
            {
                "poat": serializer.data,
            }
        )
