from django.db import models
from apps.commons.models.common_model import CommonModel


class PostObscured(CommonModel):
    """
    PostObscured Model Definition
    - post 등록시 openai의 api를 이용하여, 핵심단어를 가려 저장
    - 이 과정을 비동기로 처리하고 싶은데 어떻게 해야할지?
    - 혹은 스케줄러로 처리할까?
    """
