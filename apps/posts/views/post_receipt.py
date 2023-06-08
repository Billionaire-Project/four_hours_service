from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema

from apps.posts.serializers import PostReceiptSerializer
from apps.posts.views.receipt import callback_by_client_api


class PostReceiptCheck(APIView):
    permission_classes = [IsAuthenticated]

    """
    # PostReceipt 확인용
    ### - 해당 api가 불리면 Receipt를 확인함
    ## 해당 api가 불리는 상황
     - 로그인 시
     - WritePage 진입 시?
     - 글 작성 시?
     - 글 열람 시?
    """

    @swagger_auto_schema(
        operation_description="""
            ## receipt확인 후 권한이 있는 유저에게 반환
            """,
        responses={
            200: PostReceiptSerializer(),
        },
    )
    def get(self, request):
        result = callback_by_client_api(request.user)
        return Response(result, status=status.HTTP_200_OK)
