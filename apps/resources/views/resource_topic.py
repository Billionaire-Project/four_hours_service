from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

from apps.resources.models import Topic


class ResourceTopic(APIView):
    """
    Topic API
    """

    @swagger_auto_schema(
        operation_description="""
        # For Test
        """,
        responses={},
    )
    def get(self, request):
        tmp = Topic.objects.get(id=1)
        tmp = {
            "topic": tmp.topic,
            "content": tmp.content,
        }
        return Response(tmp, status=status.HTTP_200_OK)
