from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.posts.serializers.post import PostSerializer
from apps.posts.models.post import Post


class PostMy(APIView):
    """
    PostMy Api

    ---
    # 내가 작성한 post를 가져오는 api
    """

    def get(self, request, format=None):
        """
        method

        ---
        # 내용
        """
        posts = Post.objects.filter(user=request.user)
        if not posts:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
