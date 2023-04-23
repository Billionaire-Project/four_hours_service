from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from drf_yasg.utils import swagger_auto_schema

from apps.users.models import User
from apps.users.serializers.me import MeSerializer


class Login(APIView):
    """
    얘랑 Me랑 사실 다를게 없긴 함
    """

    @swagger_auto_schema(
        operation_description="""
        ## 로그인 시 요청하는 api
        - firebase auth login과 별개로 로그인 할때 요청해주세요
        """,
        responses={
            200: MeSerializer(),
        },
    )
    def get(self, request):
        user = User.objects.get(id=request.user.id)
        serializer = MeSerializer(user)
        return Response(serializer.data, status=HTTP_200_OK)
