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

    id = models.AutoField(primary_key=True)
    article = models.ForeignKey(
        "resources.Article",
        on_delete=models.CASCADE,
        related_name="article_summaries",
    )

    summary_content = models.TextField()
    is_used = models.BooleanField(default=False)

    # gpt feature
    time_taken = models.FloatField(null=True, blank=True)
    total_token = models.IntegerField(null=True, blank=True)
    is_failed = models.BooleanField(default=False)
