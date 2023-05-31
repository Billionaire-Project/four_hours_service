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
        posts = Post.objects.filter(
            is_obscured=False,
            is_deleted=False,
            obscured_fail=False,
        )

        post = posts[0]

        sentence = post.content

        print("debug--- sentence : ", sentence)

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            # model="gpt-4",
            messages=[
                {
                    "role": "user",
                    "content": "다음 문장의 핵심 단어만 출력해줘",
                },
                {"role": "user", "content": sentence},
            ],
        )

        result = completion.choices[0].message.content
        obscured_words = result.split(", ")

        print("debug--- obscured_words : ", obscured_words)

        obscured_content = sentence

        for word in obscured_words:
            # gpt가 이상한 단어를 뽑아줬을 경우 예외처리
            if result.__contains__(word):
                obscured_content = obscured_content.replace(word, "_" * len(word))
            else:
                is_failed = True
                break

        print(obscured_content)

        # if not result.__contains__("false"):  # 변경 가능
        #     obscured_words = result.split(", ")
        #     print("debug--- obscured_words : ", obscured_words)
        #     obscured_content = sentence
        #     for word in obscured_words:
        #         # gpt가 이상한 단어를 뽑아줬을 경우 예외처리
        #         if result.__contain__(word):
        #             obscured_content = obscured_content.replace(word, "_" * len(word))
        #         else:
        #             is_failed = True
        #             break
        #     print("debug--- obscured_content : ", obscured_content)

        return Response()
