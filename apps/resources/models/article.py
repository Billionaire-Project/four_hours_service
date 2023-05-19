from django.db import models
from apps.commons.models.common_model import CommonModel


class Article(CommonModel):
    """
    Article Model Definition
    - 크롤링해오는 아티클들 저장
    """

    class Meta:
        default_related_name = "articles"

    class ArticleKindChoices(models.TextChoices):
        SPORTS = "sports", "Sports"
        ENTERTAINMENT = "entertainment", "Entertainment"
        ETC = "etc", "Etc"

    id = models.AutoField(primary_key=True)
    kind = models.CharField(
        max_length=20,
        choices=ArticleKindChoices.choices,
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    url = models.URLField()
    is_used = models.BooleanField(default=False)
