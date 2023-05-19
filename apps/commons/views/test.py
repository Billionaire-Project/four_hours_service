from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

from apps.commons.views.pagination import Pagination
from apps.posts.serializers import PostGetSerializer, PostPostSerializer
from apps.resources.models.persona_preset import PersonaPreset
from scheduler.fake_post import gpt_fake_post_by_article


pagination = Pagination(0, 10)


class Test(APIView):
    """
    # api test용
    - 단순 테스트용입니다. 신경쓰지 마세요.
    """

    @swagger_auto_schema(
        operation_description="""
        # For Test
        """,
        # manual_parameters=page.get_params,
        responses={
            200: PostGetSerializer(many=True),
        },
    )
    def get(self, request):
        gpt_fake_post_by_article()

        return Response(status=status.HTTP_200_OK)
