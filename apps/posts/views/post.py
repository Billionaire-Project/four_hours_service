from rest_framework import status

# from rest_framework import exceptions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema

# from drf_yasg import openapi

from apps.posts.serializers import PostGetSerializer, PostPostSerializer
from apps.posts.models import Post


class Posts(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="""
        ## receipt확인 후 권한이 있는 유저에게 반환
        """,
        responses={
            200: PostGetSerializer(many=True),
        },
    )
    def get(self, request, format=None):
        # TODO: pagination
        posts = Post.objects.all()
        serializer = PostGetSerializer(
            posts,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data, status=status.HTTP_200_OK)

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
