from django.db import models
from apps.commons.models.common_model import CommonModel


class PostObscured(CommonModel):
    """
    PostObscured Model Definition
    - post 등록시 openai의 api를 이용하여, 핵심단어를 가려 저장
    - scheduler로 처리
    """

    class Meta:
        default_related_name = "post_obscureds"

    id = models.AutoField(primary_key=True)
    # 왜 null=True 인지는 모르겠음
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, null=True)
    post = models.ForeignKey("posts.Post", on_delete=models.CASCADE, null=True)
    obscured_words = models.TextField(default="")
    obscured_content = models.TextField(default="")

    # gpt feature
    time_taken = models.FloatField(null=True, blank=True)
    total_token = models.IntegerField(null=True, blank=True)
    is_failed = models.BooleanField(default=False)

    # delete option
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.obscured_content
