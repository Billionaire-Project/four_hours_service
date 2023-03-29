from django.db import models
from commons.models.common_model import CommonModel


class PostDeleteReason(CommonModel):
    """PostDeleteReason Model Definition"""
    reason = models.CharField(max_length=140)

    def __str__(self):
        return self.reason
