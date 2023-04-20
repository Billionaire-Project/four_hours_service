from django.db import models
from apps.commons.models.common_model import CommonModel


class UserSession(CommonModel):
    """
    UserSession Model Definition
    - 세션이라고 하지만, 토큰관리에 가깝다.
    - firebase auth token의 시간 관리

    - decode token 예시
    {
        'name': '이성우',
        'picture': 'https://.,..',
        'iss': 'https://...',
        'aud': '...',
        'auth_time': 1681978270,
        'user_id': '...',
        'sub': '...',
        'iat': 1681978270,
        'exp': 1681981870,
        'email': 'crescent3859@gmail.com',
        'email_verified': True,
        'firebase': {
            'identities': {
                'google.com': ['...'],
                'email': ['crescent3859@gmail.com']
            },
            'sign_in_provider': 'google.com'
        },
        'uid': '...'
    }

    auth_time: 로그인 시간
    iat: 토큰 발급 시간
    exp: 토큰 만료 시간

    사실 그렇게까지 중요하지 않으니까 이정도만 하자
    """

    class Meta:
        default_related_name = "user_sessions"

    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    login_time = models.DateTimeField(null=True, blank=True)  # auth_time
    logout_time = models.DateTimeField(null=True, blank=True)  # logout 시간
    session_expire_time = models.DateTimeField(null=True, blank=True)  # exp
    is_expired = models.BooleanField(default=False)  # logout 혹은 새로 로그인 시
