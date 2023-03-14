from django.db import models
from django.contrib.auth.models import AbstractUser

# 내가 원하는 유저 모델을 만들 수 있음, 이름을 꼭 User로 해야하는 것은 아님
# config/settings.py에 AUTH_USER_MODEL = 'users.User'를 추가해야함
# 중간에 있는 유저 데이터를 옮길 수 없으므로 프로젝트의 시작에서 만들어 줘야 함


class User(AbstractUser):
    class Meta:
        default_related_name = "users"

    uid = models.CharField(
        max_length=150,
        blank=False,
        default="",
    )
    name = models.CharField(
        max_length=150,
        blank=False,
        default="",
    )
    phone_number = models.CharField(
        max_length=20,
        blank=False,
        default="",
    )
