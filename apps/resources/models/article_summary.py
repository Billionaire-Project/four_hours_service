from django.db import models
from apps.commons.models.common_model import CommonModel


class ArticleSummary(CommonModel):
    """
    ArticleSummary Model Definition
    - 크롤링해오는 아티클의 gpt 요약본 저장
    - 500자 이상의 기사만 사용하고 요약해옴
    """

    class Meta:
        default_related_name = "article_summaries"

    class ArticleKindChoices(models.TextChoices):
        SPORTS = "sports", "Sports"
        ENTERTAINMENT = "entertainment", "Entertainment"
        ETC = "etc", "Etc"

    id = models.AutoField(primary_key=True)
    article = models.ForeignKey(
        "resources.Article",
        on_delete=models.CASCADE,
        related_name="article_summaries",
    )
    kind = models.CharField(
        max_length=20,
        choices=ArticleKindChoices.choices,
    )

    title = models.CharField(max_length=100)
    summary_content = models.TextField()
    is_used = models.BooleanField(default=False)
