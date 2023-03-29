from django.db import models
from commons.models.common_model import CommonModel


class PostLike(CommonModel):
    """PostLike Model Definition"""
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    post = models.ForeignKey("posts.Post", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} likes {self.post}"