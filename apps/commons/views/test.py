import time
import openai
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

from apps.commons.views.pagination import Pagination
from apps.posts.serializers import PostGetSerializer, PostPostSerializer
from apps.resources.models import ArticleSummary
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
        responses={
            200: PostGetSerializer(many=True),
        },
    )
    def get(self, request):
        # gpt_fake_post_by_article()
        article_summary = ArticleSummary.objects.get(id=20)

        persona = (
            PersonaPreset.objects.filter(article_kind=article_summary.article.kind)
            .order_by("?")
            .first()
        )

        print(persona)

        prompt = f"""
            기사의 요약본을 읽고, SNS에 게시할 글을 작성해주세요.
            - 기사 제목: {article_summary.article.title}
            - 기사 요약: {article_summary.summary_content}
            작성자의 특징은 다음과 같습니다.
            - 직업: {persona.job}
            - 성별: {persona.gender}
            - 연령대: {persona.age}
            - 말투: {persona.tone}
            - 성격: {[i.content for i in persona.characteristic.all()]}
            """

        print(f"{article_summary.article.title} : {persona.name} 작성 시작")

        try:
            start = time.time()
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": prompt},
                ],
            )
            end = time.time()
            print(f"time taken: {end - start}")
        except Exception as e:
            print(e)

        message = completion.choices[0].message.content

        print(message)

        return Response(
            status=status.HTTP_200_OK,
        )
