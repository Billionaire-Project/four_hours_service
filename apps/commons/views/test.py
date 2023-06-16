import datetime
import time
import openai
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

from apps.commons.views import Pagination, MyPagination
from apps.posts.models.post import Post
from apps.posts.serializers import PostGetSerializer, PostPostSerializer
from apps.posts.serializers.post_my import PostMySerializer
from apps.posts.views.receipt import callback_by_client_api
from apps.resources.models import ArticleSummary
from apps.resources.models.persona_preset import PersonaPreset
from apps.resources.models.post_generated import PostGenerated
from apps.resources.models.topic import Topic
from scheduler.random_generated_to_post import random_generated_to_post
from scheduler.fake_post import gpt_fake_post_by_article


pagination = Pagination(0, 10)

my_pagination = MyPagination(0, 10)


class Test(APIView):
    """
    # api test용
    - 단순 테스트용입니다. 신경쓰지 마세요.
    """

    @swagger_auto_schema(
        operation_description="""
        # For Test
        """,
        responses={
            200: PostGetSerializer(many=True),
        },
    )
    def get(self, request):
        # random_generated_to_post()
        tmp = PostGenerated.objects.filter(
            updated_at__gte=datetime.datetime.now() - datetime.timedelta(days=1),
        ).all()
        print(len(tmp))
        return Response(status=status.HTTP_200_OK)
