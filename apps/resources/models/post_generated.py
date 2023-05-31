from django.db import models
from apps.commons.models.common_model import CommonModel


class PostGenerated(CommonModel):
    """
    PostGenerated Model Definition
    GPT를 통해 생성된 Post
    """

    class Meta:
        default_related_name = "post_generateds"

    class PostChoices(models.TextChoices):
        NONE = "none", "None"
        ACCEPTED = "accepted", "Accepted"
        REJECTED = "rejected", "Rejected"

    id = models.AutoField(primary_key=True)
    content = models.TextField()

    article = models.ForeignKey(
        "resources.Article",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    persona_preset = models.ForeignKey(
        "resources.PersonaPreset",
        related_name="persona_presets",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    persona_situation = models.ForeignKey(
        "resources.PersonaSituation",
        related_name="persona_situations",
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

    # 관리부분
    # 해당 포스트를 체택할 것인지
    is_accepted = models.CharField(
        choices=PostChoices.choices,
        default=PostChoices.NONE,
        max_length=10,
    )
    # 검수되었는지 확인, admin에서 save하면 자동으로 True할당
    is_checked = models.BooleanField(default=False)
    # 누가 검수했는지
    who_checked = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    is_posted = models.BooleanField(default=False)

    # gpt feature
    time_taken = models.FloatField(null=True, blank=True)
    total_token = models.IntegerField(null=True, blank=True)
    is_failed = models.BooleanField(default=False)

    def __str__(self):
        # ellipsis
        if len(self.content) > 30:
            return self.content[:30] + "..."
        return self.content
