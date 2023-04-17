from rest_framework import status
from rest_framework import exceptions
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.posts.serializers.post import PostSerializer
from apps.posts.models.post import Post


# TODO: post를 get할 수 있는 자격 추가 혹은 자격에 따른 return 값 변경
class PostList(APIView):
    """
    PostList Api

    ---
    # 내용
    """

    def get(self, request, format=None):
        # TODO: pagination
        """
        post list

        ---
        # 내용
        """
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostId(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise exceptions.NotFound

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
