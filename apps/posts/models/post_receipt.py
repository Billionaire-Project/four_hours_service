from django.db import models
from apps.commons.models.common_model import CommonModel


class PostReceipt(CommonModel):
    """
    PostReceipt Model Definition
    - post 등록시 발행되는 영수증
    - 회원가입시 영수증 발행
    - 해당 영수증을 가지고 계속 사용 (근데 바뀌 수 있어서 일단 one to one으로 안만듬)
    - 이 영수증은 두가지 기능을 가짐
        1. 24시간 동안 shared post 관람 권한
        2. 4시간 동안 새로운 post 작성 금지

    글 작성 후 1회 삭제시, 글쓰기 쿨타임 및 글열람 시간은 초기화되지 않음
    다만, 열람권한은 회수
    글 작성 후 2회 삭제시, 글쓰기 쿨타임 초기화 및 열람권한 회수

    유저당 영수증 하나를 계속 사용할지 재 발급할지는 로직 더 생각해보자
    """

    class Meta:
        default_related_name = "post_receipts"

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    post = models.ForeignKey(
        "posts.Post",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    # 해당 영수증 유효여부 및 만료여부 체크
    is_valid = models.BooleanField(default=True)

    # shared post 열람권한 , 24시간
    shared_post_available_at = models.DateTimeField(null=True, blank=True)

    # 다음 글 작성 가능 시간 , 4 시간
    next_post_available_at = models.DateTimeField(null=True, blank=True)

    # post delete stack
    post_delete_stack = models.IntegerField(default=0)

    def __str__(self):
        return self.user.email
