from django.db import models
from apps.commons.models.common_model import CommonModel


class Topic(CommonModel):

    """
    Topic Model Definition
    사용자가 입력하는 혹은 GPT가 생성하는 토픽
    매일 새로운 토픽을 생성하고 각 시간마다 사용자에게 추천해줌
    - Todo : scheduler로 매일 토픽 생성하는 기능 추가
    - Todo : admin에서 토픽 추가, 삭제 기능 추가
    """

    class Meta:
        default_related_name = "topics"

    id = models.AutoField(primary_key=True)
    topic = models.CharField(max_length=100)
    content = models.CharField(max_length=1000, null=True)

    # 해당 토픽이 사용된 적 있는지
    is_used = models.BooleanField(default=False)
    # 해당 토픽이 언제 사용되었는지
    topic_used_at = models.DateTimeField(null=True)
    # 해당 토픽을 사용할 것인지 (default: True)
    is_use = models.BooleanField(default=True)
    # gpt에 의해 생성된 토픽인지
    is_generated = models.BooleanField(default=False)

    def __str__(self):
        return self.topic
