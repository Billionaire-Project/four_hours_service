from django.db import models
from apps.commons.models.common_model import CommonModel


class PersonaSituation(CommonModel):
    """PersonaSituation Model Definition"""

    class Meta:
        default_related_name = "persona_situations"

    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.content
