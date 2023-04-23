from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from drf_yasg.utils import swagger_auto_schema


from apps.users.models import UserSession


class Logout(APIView):
    """
    프론트에서 firebase auth에 토큰 만료 요청 때리고, 서버에선 세션만 닫아주면 될듯?
    """

    @swagger_auto_schema(
        operation_description="""
        ## 로그아웃 시 요청하는 api
        - firebase auth logout과 별개로 로그아웃 할때 요청해주세요
        """,
        responses={
            200: "HTTP_200_OK",
        },
    )
    def put(self, request):
        session = UserSession.objects.get(user=request.user)

        session.logout_time = timezone.now()
        session.is_expired = True
        session.save()

        return Response(status=HTTP_200_OK)
