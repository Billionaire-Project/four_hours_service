from django.db import models
from apps.commons.models.common_model import CommonModel


class Post(CommonModel):

    """
    Post Model Definition
    delete 요청시 is_deleted = True로 변경
    """

    class Meta:
        default_related_name = "posts"

    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    content = models.TextField()

    # delete option
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.title
