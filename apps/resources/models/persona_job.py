from django.db import models
from apps.commons.models.common_model import CommonModel


class PersonaJob(CommonModel):
    """PersonaJob Model Definition"""

    class Meta:
        default_related_name = "persona_jobs"

    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.content
