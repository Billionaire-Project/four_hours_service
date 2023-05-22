import datetime
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema

from apps.commons.views.pagination import Pagination

from apps.posts.serializers import PostMySerializer
from apps.posts.models import Post

pagination = Pagination(0, 10)


class PostMy(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="""
        # 내가 작성한 post를 가져옵니다.
        ### - 반환은 다음과 같습니다.
        ### - posts: 날짜별로 정렬된 post들을 반환합니다.
        ```
        {
            "start": 0,
            "offset": 10,
            "next": 10,
            "posts": {
                    "2023-05-06": [
                        {
                            "id": 53,
                            "content": "~~~",
                            "created_at": "2023-05-06T16:47:57.651504+09:00",
                            "updated_at": "2023-05-06T16:48:01.421320+09:00"
                        },
                        ....
                },
                
        }
        ```
        ### - 다음 요청시에는 next값을 start로 요청해주세요!
        ### - next가 null이면 더이상 요청할 데이터가 없습니다.
        ### - 날짜별로 쓴 글이 정렬되어 내려갑니다.
        """,
        manual_parameters=pagination.get_params,
    )
    def get(self, request, format=None):
        queryset = Post.objects.filter(is_deleted=False, user=request.user).order_by(
            "-created_at"
        )
        result = pagination.get(request, queryset)
        serializer = PostMySerializer(
            result.pop("result"),
            many=True,
        )

        # serializer.data의 인자를 날짜별로 묶어서 반환
        posts_by_date = {}
        for post in serializer.data:
            if post["created_at"][:10] == str(datetime.date.today()):
                post["created_at"] = "Today"
            elif post["created_at"][:10] == str(
                datetime.date.today() - datetime.timedelta(days=1)
            ):
                post["created_at"] = "Yesterday"
            else:
                post["created_at"] = post["created_at"][:10]

            if post["created_at"] not in posts_by_date:
                posts_by_date[post["created_at"]] = [post]
            else:
                posts_by_date[post["created_at"]].append(post)

        result["posts"] = posts_by_date

        return Response(result)
