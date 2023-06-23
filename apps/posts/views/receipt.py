from datetime import datetime, timedelta
from pickle import FALSE
from typing import Optional
from apps.users.models import User
from apps.posts.models import Post, PostReceipt


"""
Receipt 관련 로직 정리
TODO: Debuging용으로 4시간 짜리를 1분 짜리로 바꿔둠
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
        # updated_at__gte=datetime.now() - timedelta(hours=4),
        updated_at__gte=datetime.now() - timedelta(minutes=1),
        user=user.id,
    )
    return queryset.exists()


# 4시간 이내에 몇번이나 삭제했는지 확인
def post_delete_count_check(user: User) -> int:
    queryset = Post.objects.filter(
        is_deleted=True,
        # updated_at__gte=datetime.now() - timedelta(hours=4),
        updated_at__gte=datetime.now() - timedelta(minutes=1),
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
                # updated_at__gte=datetime.now() - timedelta(hours=4),
                updated_at__gte=datetime.now() - timedelta(minutes=1),
                user=user.id,
            )
            .order_by("-updated_at")
            .first()
        )
        result["is_readable"] = False
        result["readable_ended_at"] = None
        result["is_postable"] = False
        # result["postable_at"] = last_deleted_post.updated_at + timedelta(hours=4)
        result["postable_at"] = last_deleted_post.updated_at + timedelta(minutes=1)
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
                # updated_at__gte=datetime.now() - timedelta(hours=4),
                updated_at__gte=datetime.now() - timedelta(minutes=1),
                user=user.id,
            )
            .order_by("-updated_at")
            .first()
        )
        result["is_postable"] = False
        # result["postable_at"] = queryset.updated_at + timedelta(hours=4)
        result["postable_at"] = queryset.updated_at + timedelta(minutes=1)
    else:
        result["is_postable"] = True
        result["postable_at"] = None

    return result
