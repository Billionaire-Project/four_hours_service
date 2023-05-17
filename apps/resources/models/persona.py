from django.db import models
from apps.commons.models.common_model import CommonModel


class Persona(CommonModel):
    """
    Persona Model Definition
    Fake Post를 작성하는 가상의 사용자를 정의하기 위한 페르소나
    범주:
    - 직업
    - 성별
    - 연령대
    - 말투
    - 상황 : 가상의 인물이 처한 상황
    - 캐릭터 : 가상의 인물의 특징
    - 주제
    """

    class Meta:
        default_related_name = "personas"

    class PersonaKindChoices(models.TextChoices):
        JOB = "job", "Job"
        GENDER = "gender", "Gender"
        AGE = "age", "Age"
        TONE = "tone", "Tone"
        SITUATION = "situation", "Situation"
        CHARACTERISTIC = "characteristic", "Characteristic"
        TOPIC = "topic", "Topic"

    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=100)
    kind = models.CharField(
        max_length=20,
        choices=PersonaKindChoices.choices,
    )
    is_active = models.BooleanField(default=True)
