from django.db import models
from django.contrib.auth.models import AbstractUser

# 내가 원하는 유저 모델을 만들 수 있음, 이름을 꼭 User로 해야하는 것은 아님
# config/settings.py에 AUTH_USER_MODEL = 'users.User'를 추가해야함
# 중간에 있는 유저 데이터를 옮길 수 없으므로 프로젝트의 시작에서 만들어 줘야 함

# 소셜이 정해지면 유저 테이블 수정해야 함


class User(AbstractUser):
    class Meta:
        default_related_name = "users"

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

    def __str__(self):
        return self.email
