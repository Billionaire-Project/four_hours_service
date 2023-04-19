from rest_framework import status

# from rest_framework import exceptions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema

# from drf_yasg import openapi

from apps.posts.serializers import PostObscuredSerializer
from apps.posts.models import PostObscured


class PostsObscured(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="""
        ## receipt확인 후 권한이 없는 유저에게 반환
        """,
        responses={
            200: PostObscuredSerializer(many=True),
        },
    )
    def get(self, request, format=None):
        # TODO: pagination
        obscured_posts = PostObscured.objects.all()
        serializer = PostObscuredSerializer(
            obscured_posts,
            many=True,
        )
        return Response(serializer.data, status=status.HTTP_200_OK)
