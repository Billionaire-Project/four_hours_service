from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema

from apps.posts.models import PostReceipt
from apps.posts.serializers import PostReceiptSerializer


class PostReceiptCheck(APIView):
    permission_classes = [IsAuthenticated]

    """
    # PostReceipt 확인용
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
        post_receipt = PostReceipt.objects.get(user_id=request.user.id)
        serializer = PostReceiptSerializer(post_receipt)
        return Response(serializer.data, status=status.HTTP_200_OK)
