from django.db import models
from apps.commons.models.common_model import CommonModel


class Post(CommonModel):
    """Post Model Definition"""
    title = models.CharField(max_length=140)
    content = models.TextField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
