from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from drf_yasg.utils import swagger_auto_schema
from django.utils import timezone
from firebase_admin import auth

from apps.users.models import User
from apps.users.models import UserSession


class Test(APIView):
    """
    # api test용
    - 단순 테스트용입니다. 신경쓰지 마세요.
    """

    def get(self, request):
        # auth_header = request.META.get("HTTP_AUTHORIZATION")
        # print("debug--- auth_header", auth_header)
        # id_token = auth_header.split(" ").pop()
        # print("debug--- id_token", id_token)
        # decoded_token = auth.verify_id_token(id_token)
        # print("debug--- decoded_token", decoded_token)
        # uid = decoded_token.get("uid")
        # print("debug--- uid", uid)
        sessions = UserSession.objects.all()

        print("debug--- sessions", sessions)
        print("debug--- sessions", sessions.last())

        # for session in sessions:
        #     if not session.is_expired:
        #         print("debug--- session", session.is_expired)
        #         session.logout_time = timezone.now()
        #         session.is_expired = True
        #         session.save()

        # print("debug--- session", sessions[0].is_expired)

        # last element of sessions

        return Response(status=HTTP_200_OK)

    # def put(self, request):
    #     # 토큰 만료
    #     auth_header = request.META.get("HTTP_AUTHORIZATION")
    #     print("debug--- auth_header", auth_header)
    #     id_token = auth_header.split(" ").pop()
    #     print("debug--- id_token", id_token)
    #     decoded_token = auth.verify_id_token(id_token)
    #     print("debug--- decoded_token", decoded_token)
    #     uid = decoded_token.get("uid")
    #     print("debug--- uid", uid)
    #     auth.revoke_refresh_tokens(uid)

    #     # session = UserSession.objects.get(user=request.user) # 이거 필터로 가져오자

    #     # session.logout_time = timezone.now()
    #     # session.is_expired = True
    #     # session.save()

    #     return Response(status=HTTP_200_OK)

    # import time
    #     import openai

    #     openai.api_key = "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"

    #     post = Post.objects.get(id=2)
    #     sentence = post.content

    #     start = time.time()
    #     completion = openai.ChatCompletion.create(
    #         model="gpt-3.5-turbo",
    #         # model="gpt-4",
    #         messages=[
    #             {"role": "user", "content": "다음 문장의 핵심 단어만 출력해줘 불가능하다면 false를 출력해줘"},
    #             {"role": "user", "content": sentence},
    #         ],
    #     )
    #     # 종료 시간 체크
    #     end = time.time()

    #     total_time = end - start

    #     result = completion.choices[0].message.content

    #     total_token = completion.usage.total_tokens

    #     if result == "false":
    #         return Response("false", status=status.HTTP_200_OK)
    #     else:
    #         word_list = result.split(", ")

    #         for word in word_list:
    #             sentence = sentence.replace(word, "_" * len(word))

    #         return Response(
    #             {
    #                 "result": result,
    #                 "sentence": sentence,
    #                 "total_time": total_time,
    #                 "total_token": total_token,
    #             }
    #         )
