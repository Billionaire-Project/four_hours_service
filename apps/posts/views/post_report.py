from rest_framework import status
from rest_framework import exceptions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema

from apps.posts.models import Post, PostReport


class PostReportId(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            post = Post.objects.get(id=pk)
            return post
        except post.DoesNotExist:
            raise exceptions.NotFound

    @swagger_auto_schema(
        operation_description="""
        # post를 신고합니다.
        ### - post_id를 path parameter로 받습니다.
        ### - 신고는 한번만 가능합니다.
        ### - 한번 신고한 post는 신고 철회가 불가능합니다.
        ### - 신고된 post는 해당 사용자에게 노출되지 않습니다.
        ### - 요청한 포스트가 삭제되었다면 404를 반환합니다.
        """,
    )
    def post(self, request, pk, format=None):
        post = self.get_object(pk)
        if post.is_deleted:
            raise exceptions.NotFound

        post_report = PostReport.objects.create(
            user=request.user,
            post=post,
        )
        post_report.save()

        return Response(status=status.HTTP_200_OK)
