from django.db import models
from django.contrib.auth.models import AbstractUser

# 내가 원하는 유저 모델을 만들 수 있음, 이름을 꼭 User로 해야하는 것은 아님
# config/settings.py에 AUTH_USER_MODEL = 'users.User'를 추가해야함
# 중간에 있는 유저 데이터를 옮길 수 없으므로 프로젝트의 시작에서 만들어 줘야 함

# 소셜이 정해지면 유저 테이블 수정해야 함


class User(AbstractUser):
    class Meta:
        default_related_name = "users"

    id = models.AutoField(primary_key=True)
    # firebase auth uuid
    uid = models.CharField(
        max_length=150,
        blank=False,
        default="",
    )
    # from firebase auth
    name = models.CharField(
        max_length=150,
        null=True,
        blank=True,
        default="",
    )
    firebase_picture = models.URLField(
        max_length=255,
        null=True,
        blank=True,
        default="",
    )

    first_name = None
    last_name = None

    # delete option
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    # deleted_reason
    # 재가입시 패널티 없고 아예 새로운 아이디로 다시 시작
    # firebase auth에서까지 삭제

    def __str__(self):
        return f"{self.id}_{self.username}"
