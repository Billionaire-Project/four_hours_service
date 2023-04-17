from django.db import models
from apps.commons.models.common_model import CommonModel


class PostDeleteReason(CommonModel):
    """PostDeleteReason Model Definition"""
    reason = models.CharField(max_length=140)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.reason
