from datetime import datetime, timedelta
from pickle import FALSE
from typing import Optional
from apps.users.models import User
from apps.posts.models import Post, PostReceipt


"""
Receipt 관련 로직 정리
TODO:
이거 하다보니까 개빡센데, 이거 이걸로 정리하는게 아니라, 그냥 그떄그때 로직 처리하는게 나을지도???
분기 처리도 빡세니까
is_readable is_postable 함수 다 파서 쓰는게 나을지도
메서드 최대한 단순하게, 역할을 하나만!
"""


# 24시간 이내에 쓰여진 post가 있는지 확인
def post_in_24(user: User) -> bool:
    queryset = Post.objects.filter(
        is_deleted=False,
        updated_at__gte=datetime.now() - timedelta(days=1),
        user=user.id,
    )
    return queryset.exists()


# 4시간 이내에 쓰여진 post가 있는지 확인
def post_in_4(user: User) -> bool:
    queryset = Post.objects.filter(
        is_deleted=False,
        updated_at__gte=datetime.now() - timedelta(hours=4),
        user=user.id,
    )
    return queryset.exists()


# 4시간 이내에 몇번이나 삭제했는지 확인
def post_delete_count_check(user: User) -> int:
    queryset = Post.objects.filter(
        is_deleted=True,
        updated_at__gte=datetime.now() - timedelta(hours=4),
        user=user.id,
    )

    return queryset.count()


def callback_by_client_api(user: User) -> dict:
    deleted_stack = post_delete_count_check(user)

    result = {
        "is_postable": None,
        "is_readable": None,
        "readable_ended_at": None,
        "postable_at": None,
        "post_delete_stack": deleted_stack,
    }

    if deleted_stack >= 2:
        last_deleted_post = (
            Post.objects.filter(
                is_deleted=True,
                updated_at__gte=datetime.now() - timedelta(hours=4),
                user=user.id,
            )
            .order_by("-updated_at")
            .first()
        )
        result["is_readable"] = False
        result["readable_ended_at"] = None
        result["is_postable"] = False
        result["postable_at"] = last_deleted_post.updated_at + timedelta(hours=4)
        return result

    if post_in_24(user):
        queryset = (
            Post.objects.filter(
                is_deleted=False,
                updated_at__gte=datetime.now() - timedelta(days=1),
                user=user.id,
            )
            .order_by("-updated_at")
            .first()
        )
        result["is_readable"] = True
        result["readable_ended_at"] = queryset.updated_at + timedelta(days=1)
    else:
        result["is_readable"] = False
        result["readable_ended_at"] = None

    if post_in_4(user):
        queryset = (
            Post.objects.filter(
                is_deleted=False,
                updated_at__gte=datetime.now() - timedelta(hours=4),
                user=user.id,
            )
            .order_by("-updated_at")
            .first()
        )
        result["is_postable"] = False
        result["postable_at"] = queryset.updated_at + timedelta(hours=4)
    else:
        result["is_postable"] = True
        result["postable_at"] = None

    return result


# class Receipt:
#     @staticmethod
#     def post_exist_check(user: User) -> bool:
#         queryset = Post.objects.filter(
#             is_deleted=False,
#             updated_at__gte=datetime.now() - timedelta(days=1),
#             user=user.id,
#         )
#         return queryset.exists()

#     def callback_when_post_get(self, user: User) -> bool:
#         print("callback_when_post_get")
#         # post를 불러올 때, post를 줄지 obscured를 줄지 결정
#         receipt = PostReceipt.objects.get(user=user)
#         # is_readable이 True면 True를 반환
#         if receipt.is_readable:
#             return True
#         else:
#             print("is_readable is False")
#             # 아니라면 post가 존재하는지 확인
#             if self.post_exist_check(user):
#                 print("post_exist_check is True")
#                 # post가 존재한다면, 내가 작성한 마지막 post의 정보를 가져와서 receipt를 업데이트 후 True를 반환
#                 post = Post.objects.filter(
#                     is_deleted=False,
#                     updated_at__gte=datetime.now() - timedelta(days=1),
#                     user=user.id,
#                 ).order_by("-updated_at")[0]
#                 self.receipt_update(
#                     user=user,
#                     post=post,
#                     is_postable=False,
#                     is_readable=True,
#                     posted_time=post.updated_at,
#                 )
#                 return True
#             else:
#                 # post가 존재하지 않는다면, receipt를 업데이트 후 False를 반환
#                 self.receipt_update(
#                     user=user,
#                     is_postable=True,
#                     is_readable=False,
#                     posted_time=None,
#                 )
#         return False

#     def callback_when_post_post(self, user: User, post: Post):
#         pass

#     def callback_when_post_delete(self, user: User, post: Post):
#         pass

#     def receipt_update(
#         self,
#         user: User,
#         post: Optional[Post] = None,
#         is_postable: Optional[bool] = None,
#         is_readable: Optional[bool] = None,
#         posted_time: Optional[datetime] = None,
#         post_delete_stack: Optional[int] = None,
#     ):
#         receipt = PostReceipt.objects.get(user=user)
#         if post:
#             receipt.post = post
#         if is_postable is not None:
#             receipt.is_postable = is_postable
#         if is_readable is not None:
#             receipt.is_readable = is_readable
#         if posted_time:
#             receipt.postable_at = posted_time + timedelta(hours=4)
#             receipt.readable_ended_at = posted_time + timedelta(days=1)
#         if post_delete_stack == 0:
#             receipt.post_delete_stack = 0
#         elif post_delete_stack == 1:
#             receipt.post = None
#             receipt.is_postable = True
#             receipt.is_readable = False
#             receipt.postable_at = None
#             receipt.readable_ended_at = None
#             receipt.post_delete_stack = 1
#         elif post_delete_stack == 2:
#             receipt.post = None
#             receipt.is_postable = False
#             receipt.is_readable = False
#             receipt.postable_at = datetime.now() + timedelta(hours=4)
#             receipt.readable_ended_at = None
#             receipt.post_delete_stack = 2

#         receipt.save()
