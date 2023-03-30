from django.db import models
from apps.commons.models.common_model import CommonModel


class PostReport(CommonModel):
    """PostReport Model Definition"""
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    post = models.ForeignKey("posts.Post", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} reports {self.post}"
