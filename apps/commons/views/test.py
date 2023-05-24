import time
import openai
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

from apps.commons.views.pagination import Pagination
from apps.posts.serializers import PostGetSerializer, PostPostSerializer
from apps.resources.models.article import Article
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
        article = Article.objects.get(id=172)

        prompt = f"""
            다음 기사를 한국어로 요약해주세요.
            - 기사 제목: {article.title}
            - 기사 내용: {article.content}
            """

        start = time.time()
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt},
            ],
        )
        end = time.time()

        print(f"걸린시간: {end - start}")
        message = completion.choices[0].message.content
        print(message)

        random_persona = PersonaPreset.objects.order_by("?").first()

        prompt = f"""
            아래와 같은 기사가 있습니다. 이 기사를 바탕으로 트위터에 게시할 글을 작성해주세요.
            - 기사 제목: {article.title}
            - 기사 내용: {message}
            작성자의 특징은 다음과 같습니다.
            - 직업: {random_persona.job}
            - 성별: {random_persona.gender}
            - 연령대: {random_persona.age}
            - 말투: {random_persona.tone}
            - 성격: {[i.content for i in random_persona.characteristic.all()]}
            """

        print(f"{article.title} : {random_persona.name} 작성 시작")

        try:
            start = time.time()
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": prompt},
                ],
            )
            end = time.time()
        except Exception as e:
            print(e)
            time.sleep(10)

        message = completion.choices[0].message.content

        print(message)

        return Response(
            status=status.HTTP_200_OK,
        )
