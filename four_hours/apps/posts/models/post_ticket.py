from django.db import models
from apps.commons.models.common_model import CommonModel


class PostTicket(CommonModel):
    """
    PostTicket Model Definition
    - post 등록시 발행되는 티켓
    - 이 티켓은 두가지 기능을 가짐
        1. 24시간 동안 shared post 관람 권한
        2. 4시간 동안 새로운 post 작성 금지
    """
