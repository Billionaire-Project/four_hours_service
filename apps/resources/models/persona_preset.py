from django.db import models
from apps.commons.models.common_model import CommonModel


class PersonaPreset(CommonModel):
    """
    PersonaPreset Model Definition
    사전 설정된 가상의 유저 페르소나
    """

    class Meta:
        default_related_name = "persona_presets"

    class AgeChoices(models.TextChoices):
        TEEN = "10대", "10대"
        TWENTY = "20대", "20대"
        THIRTY = "30대", "30대"
        FORTY = "40대", "40대"
        FIFTY = "50대", "50대"
        SIXTY = "60대", "60대"

    class GenderChoices(models.TextChoices):
        MALE = "남성", "남성"
        FEMALE = "여성", "여성"

    class ArticleKindChoices(models.TextChoices):
        SPORTS = "sports", "Sports"
        ENTERTAINMENT = "entertainment", "Entertainment"

    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=100, null=True, blank=True)

    age = models.CharField(
        max_length=20,
        choices=AgeChoices.choices,
    )
    gender = models.CharField(
        max_length=20,
        choices=GenderChoices.choices,
    )
    article_kind = models.CharField(
        max_length=20,
        choices=ArticleKindChoices.choices,
        default=ArticleKindChoices.SPORTS,
    )

    job = models.ForeignKey(
        "resources.PersonaJob",
        on_delete=models.SET_NULL,
        related_name="persona_presets",
        null=True,
        blank=True,
    )
    tone = models.ForeignKey(
        "resources.PersonaTone",
        on_delete=models.SET_NULL,
        related_name="persona_presets",
        null=True,
        blank=True,
    )
    characteristic = models.ManyToManyField(
        "resources.PersonaCharacteristic",
        related_name="persona_presets",
        blank=True,
    )

    def __str__(self):
        return self.name
