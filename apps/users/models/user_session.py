from django.db import models
from apps.commons.models.common_model import CommonModel


class UserSession(CommonModel):
    """
    UserSession Model Definition
    - 세션이라고 하지만, 토큰관리에 가깝다.
    - firebase auth token의 시간 관리
    """

    class Meta:
        default_related_name = "user_sessions"

    class SocialKindChoices(models.TextChoices):
        GOOGLE = "google", "Google"
        APPLE = "apple", "Apple"

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)

    issued_at = models.DateTimeField(auto_now_add=True)  # iat
    accessed_at = models.DateTimeField(auto_now_add=True, null=True)  # iat
    logged_out_at = models.DateTimeField(null=True, default=None)  # logout 시간
    expired_at = models.DateTimeField(null=True, blank=True)  # exp

    social = models.CharField(
        max_length=20,
        choices=SocialKindChoices.choices,
    )
    count = models.PositiveBigIntegerField(default=0)


"""
- decode token 예시
{
   "name":"이성우",
   "picture":"https://lh3.googleusercontent.com/a/AGNmyxaGm9IDqEQ3LEzm7vnWnk6blCUAuOBF377a6y5Njg=s96-c",
   "iss":"https://securetoken.google.com/four-hours-5d3dd",
   "aud":"four-hours-5d3dd",
   "auth_time":1682578035,
   "user_id":"JHqWSoLmNlbJGSojQ3156wf3Mrp2",
   "sub":"JHqWSoLmNlbJGSojQ3156wf3Mrp2",
   "iat":1682698340,
   "exp":1682701940,
   "email":"crescent3859@gmail.com",
   "email_verified":true,
   "firebase":{
      "identities":{
         "google.com":[
            "106066955300738489270"
         ],
         "email":[
            "crescent3859@gmail.com"
         ]
      },
      "sign_in_provider":"google.com"
   },
   "uid":"JHqWSoLmNlbJGSojQ3156wf3Mrp2"
}


{
   "iss":"https://securetoken.google.com/four-hours-5d3dd",
   "aud":"four-hours-5d3dd",
   "auth_time":1682700065,
   "user_id":"lljpAU4qU9fnkoQ8YOaLbGgjKKa2",
   "sub":"lljpAU4qU9fnkoQ8YOaLbGgjKKa2",
   "iat":1682700065,
   "exp":1682703665,
   "email":"lukaid@icloud.com",
   "email_verified":true,
   "firebase":{
      "identities":{
         "apple.com":[
            "000908.ceba0c60fbf941328cf5929003eefb4d.0525"
         ],
         "email":[
            "lukaid@icloud.com"
         ]
      },
      "sign_in_provider":"apple.com"
   },
   "uid":"lljpAU4qU9fnkoQ8YOaLbGgjKKa2"
}


    auth_time: 로그인 시간
    iat: 토큰 발급 시간
    exp: 토큰 만료 시간


"""
