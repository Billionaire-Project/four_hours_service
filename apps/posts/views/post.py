from rest_framework import status

# from rest_framework import exceptions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema

# from drf_yasg import openapi

from apps.posts.serializers import PostGetSerializer, PostPostSerializer
from apps.posts.models import Post

from drf_yasg import openapi

get_params = [
    openapi.Parameter(
        "start",
        openapi.IN_QUERY,
        description="시작",
        type=openapi.TYPE_INTEGER,
        default=0,
    ),
    openapi.Parameter(
        "offset",
        openapi.IN_QUERY,
        description="개수",
        type=openapi.TYPE_INTEGER,
        default=10,
    ),
]


class Posts(APIView):
    permission_classes = [IsAuthenticated]

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
        manual_parameters=get_params,
        responses={
            200: PostGetSerializer(many=True),
        },
    )
    def get(self, request, format=None):
        start = int(request.query_params.get("start", 0))
        offset = int(request.query_params.get("offset", 10))

        posts = Post.objects.all()[start : start + offset]
        serializer = PostGetSerializer(
            posts,
            many=True,
            context={"request": request},
        )
        return Response(
            {
                "start_from": start,
                "offset": offset,
                "posts": serializer.data,
                "status": status.HTTP_200_OK,
            }
        )

    @swagger_auto_schema(
        operation_description="post를 작성합니다.",
        request_body=PostPostSerializer,
        responses={
            200: PostPostSerializer(),
        },
    )
    def post(self, request, format=None):
        """

        ---
        포스트 작성
        """
        serializer = PostPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="""
        # 금방 지울 테스트용입니다. 신경쓰지 마세요
        """,
    )
    def put(self, request, format=None):
        import time
        import openai

        openai.api_key = "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"

        post = Post.objects.get(id=2)
        sentence = post.content

        start = time.time()
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            # model="gpt-4",
            messages=[
                {"role": "user", "content": "다음 문장의 핵심 단어만 출력해줘 불가능하다면 false를 출력해줘"},
                {"role": "user", "content": sentence},
            ],
        )
        # 종료 시간 체크
        end = time.time()

        total_time = end - start

        result = completion.choices[0].message.content

        total_token = completion.usage.total_tokens

        if result == "false":
            return Response("false", status=status.HTTP_200_OK)
        else:
            word_list = result.split(", ")

            for word in word_list:
                sentence = sentence.replace(word, "_" * len(word))

            return Response(
                {
                    "result": result,
                    "sentence": sentence,
                    "total_time": total_time,
                    "total_token": total_token,
                }
            )
