from django.db import models
from apps.commons.models.common_model import CommonModel


class Article(CommonModel):
    """
    Article Model Definition
    - 크롤링해오는 아티클들 저장
    """

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    url = models.URLField()
