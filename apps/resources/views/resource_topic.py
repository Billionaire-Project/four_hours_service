from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

from apps.resources.models import Topic


class ResourceTopic(APIView):
    """
    # api test용
    - 단순 테스트용입니다. 신경쓰지 마세요.
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
        }
        return Response(tmp, status=status.HTTP_200_OK)
