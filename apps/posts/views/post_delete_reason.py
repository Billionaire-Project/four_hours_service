from rest_framework import status
from rest_framework import exceptions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema

from apps.posts.serializers import PostDeleteReasonSerializer
from apps.posts.models import PostDeleteReason


class PostDeleteReasons(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        post_delete_reason = PostDeleteReason.objects.filter(is_public=True)
        serializer = PostDeleteReasonSerializer(post_delete_reason, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
