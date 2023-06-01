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
from apps.posts.views.receipt import Receipt
from apps.resources.models import ArticleSummary
from apps.resources.models.persona_preset import PersonaPreset
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
        # get posts within 24 hours
        # posts = (
        #     Post.objects.filter(
        #         updated_at__gte=datetime.datetime.now() - datetime.timedelta(days=1)
        #     )
        #     .order_by("-updated_at")
        #     .all()
        # )

        # serializer = PostGetSerializer(posts, many=True, context={"request": request})
        # result = serializer.data

        result = Receipt.post_exist_check(request.user)

        return Response(result)
