from django.db import models
from apps.commons.models.common_model import CommonModel


class Post(CommonModel):

    """
    Post Model Definition
    delete 요청시 is_deleted = True로 변경
    """

    class Meta:
        default_related_name = "posts"

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    content = models.TextField()

    # delete option
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted_reason = models.ForeignKey(
        "posts.PostDeleteReason",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    # gpt obsured
    is_obscured = models.BooleanField(default=False)

    # gpt generated
    is_generated = models.BooleanField(default=False)
    generated_post = models.ForeignKey(
        "resources.PostGenerated",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.content
