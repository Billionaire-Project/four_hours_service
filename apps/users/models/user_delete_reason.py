from django.db import models
from apps.commons.models.common_model import CommonModel


class UserDeleteReason(CommonModel):
    """UserDeleteReason Model Definition"""

    id = models.AutoField(primary_key=True)
    reason = models.CharField(max_length=140)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.reason
