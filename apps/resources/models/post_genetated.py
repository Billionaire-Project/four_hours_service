from django.db import models
from apps.commons.models.common_model import CommonModel


class PostGenerated(CommonModel):
    """
    PostGenerated Model Definition
    GPT를 통해 생성된 Post
    """

    class Meta:
        default_related_name = "post_generateds"

    id = models.AutoField(primary_key=True)
    content = models.TextField()
    # article = models.ForeignKey(

    persona_job = models.ForeignKey(
        "resources.Persona",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    persona_gender = models.ForeignKey(
        "resources.Persona",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    persona_age = models.ForeignKey(
        "resources.Persona",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    persona_tone = models.ForeignKey(
        "resources.Persona",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    persona_situation = models.ForeignKey(
        "resources.Persona",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    persona_characteristic = models.ForeignKey(
        "resources.Persona",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    persona_topic = models.ForeignKey(
        "resources.Persona",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    topic = models.ForeignKey(
        "resources.Topic",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(default=True)

    # gpt feature
    time_taken = models.FloatField(null=True, blank=True)
    total_token = models.IntegerField(null=True, blank=True)
    is_failed = models.BooleanField(default=False)
