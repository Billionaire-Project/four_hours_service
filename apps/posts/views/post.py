from rest_framework import status

# from rest_framework import exceptions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema

# from drf_yasg import openapi

from apps.posts.serializers import PostGetSerializer, PostPostSerializer
from apps.posts.models import Post

from drf_yasg import openapi

get_params = [
    openapi.Parameter(
        "start",
        openapi.IN_QUERY,
        description="시작",
        type=openapi.TYPE_INTEGER,
        default=0,
    ),
    openapi.Parameter(
        "offset",
        openapi.IN_QUERY,
        description="개수",
        type=openapi.TYPE_INTEGER,
        default=10,
    ),
]


class Posts(APIView):
    permission_classes = [IsAuthenticated]

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
        manual_parameters=get_params,
        responses={
            200: PostGetSerializer(many=True),
        },
    )
    def get(self, request, format=None):
        start = int(request.query_params.get("start", 0))
        offset = int(request.query_params.get("offset", 10))

        posts = Post.objects.all()[start : start + offset]
        serializer = PostGetSerializer(
            posts,
            many=True,
            context={"request": request},
        )
        return Response(
            {
                "start_from": start,
                "offset": offset,
                "posts": serializer.data,
                "status": status.HTTP_200_OK,
            }
        )

    @swagger_auto_schema(
        operation_description="post를 작성합니다.",
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
