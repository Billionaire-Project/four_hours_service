import time
import openai
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from django.utils import timezone
from firebase_admin import auth
from apps.commons.views.pagination import Pagination
from apps.posts.serializers.post_my import PostMySerializer
from apps.posts.serializers.post_receipt import PostReceiptSerializer
from apps.resources.models import Persona
from apps.resources.models.article import Article
from apps.resources.models.post_genetated import PostGenerated

from apps.users.models import User
from apps.users.models import UserSession
from apps.users.serializers.serializers import UserSerializer
from apps.posts.models import Post, PostReceipt
from apps.posts.serializers import PostGetSerializer, PostPostSerializer
from scheduler.news_crawling_entertain import crawling_entertain_news
from scheduler.news_crawling_sports import crawling_sports_news


pagination = Pagination(0, 10)


class Test(APIView):
    """
    # api test용
    - 단순 테스트용입니다. 신경쓰지 마세요.
    """

    def gpt_fake_post(
        self,
        job="",
        gender="",
        age="",
        tone="",
        situation="",
        characteristic="",
        topic="",
        article_title="",
        article_content="",
    ):
        # 트위터에 게시해 달라하니까 자꾸 해시태그 담...
        # prompt = f"""
        #     다음 조건에 맞춰 트위터에 게시할 글을 작성해주세요.
        #     - 직업: {job}
        #     - 성별: {gender}
        #     - 연령대: {age}
        #     - 말투: {tone}
        #     - 상황: {situation}
        #     - 캐릭터: {characteristic}
        #     - 주제: {topic}
        #     """

        prompt = f"""
            아래와 같은 기사가 있습니다. 이 기사를 바탕으로 트위터에 게시할 글을 작성해주세요.
            - 기사 제목: {article_title}
            - 기사 내용: {article_content}
            작성자의 특징은 다음과 같습니다.
            - 직업: {job}
            - 성별: {gender}
            - 연령대: {age}
            - 말투: {tone}
            """

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt},
            ],
        )

        message = completion.choices[0].message.content
        token = completion.usage.total_tokens

        return message, token

    @swagger_auto_schema(
        operation_description="""
        ## receipt확인 후 권한이 있는 유저에게 반환
        - 반환은 다음과 같다
        ```
        {
            "start_from": 0,
            "offset": 10,
            "posts": [...],
            "status": 200
        }
        ```
        - 다음 요청시에는 start_from에 offset을 더한 값으로 요청해주세요
        """,
        # manual_parameters=page.get_params,
        responses={
            200: PostGetSerializer(many=True),
        },
    )
    def get(self, request):
        articles = Article.objects.all()
        # get random persona
        for article in articles:
            print(article.title)
            persona_job = (
                Persona.objects.filter(kind="job", is_active=True).order_by("?").first()
            )
            persona_gender = (
                Persona.objects.filter(kind="gender", is_active=True)
                .order_by("?")
                .first()
            )
            persona_age = (
                Persona.objects.filter(kind="age", is_active=True).order_by("?").first()
            )
            persona_tone = (
                Persona.objects.filter(kind="tone", is_active=True)
                .order_by("?")
                .first()
            )

            start = time.time()
            message, token = self.gpt_fake_post(
                article_title=article.title,
                article_content=article.content,
                job=persona_job.content,
                gender=persona_gender.content,
                age=persona_age.content,
                tone=persona_tone.content,
                # situation=persona_situation.content,
                # characteristic=persona_characteristic.content,
                # topic=persona_topic.content,
            )
            end = time.time()

            PostGenerated.objects.create(
                content=message,
                persona_job=persona_job,
                persona_gender=persona_gender,
                persona_age=persona_age,
                persona_tone=persona_tone,
                # persona_situation=persona_situation,
                # persona_characteristic=persona_characteristic,
                # persona_topic=persona_topic,
                total_token=token,
                article=article,
                time_taken=end - start,
            )

        return Response(status=status.HTTP_200_OK)
        # queryset = Post.objects.filter(is_deleted=False, user=request.user).order_by(
        #     "-created_at"
        # )
        # result = pagination.get(request, queryset)
        # serializer = PostMySerializer(
        #     result.pop("result"),
        #     many=True,
        # )
        # # serializer.data의 인자를 날짜별로 묶어서 반환
        # posts_by_date = {}
        # for post in serializer.data:
        #     if post["created_at"][:10] not in posts_by_date:
        #         posts_by_date[post["created_at"][:10]] = [post]
        #     else:
        #         posts_by_date[post["created_at"][:10]].append(post)

        # result["posts"] = posts_by_date

        # # print(request.user.post_reports.all())

        # return Response(result)

        # 여기서는 단순 확인기능만, PostReceipt 관련 테스트
        # post_receipt = PostReceipt.objects.get(user_id=request.user.id)
        # serializer = PostReceiptSerializer(post_receipt)

        # return Response(serializer.data)
