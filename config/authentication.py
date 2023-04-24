import os

from django.utils import timezone

from apps.users.models import User, UserSession
from apps.posts.models import PostReceipt
from firebase_admin import auth
from firebase_admin import credentials
from firebase_admin import initialize_app
from rest_framework import authentication, exceptions

from .exceptions import FirebaseError
from .exceptions import NoAuthToken

cred = credentials.Certificate(
    {
        "type": os.environ.get("FIREBASE_ACCOUNT_TYPE"),
        "project_id": os.environ.get("FIREBASE_PROJECT_ID"),
        "private_key_id": os.environ.get("FIREBASE_PRIVATE_KEY_ID"),
        "private_key": os.environ.get("FIREBASE_PRIVATE_KEY").replace("\\n", "\n"),
        "client_email": os.environ.get("FIREBASE_CLIENT_EMAIL"),
        "client_id": os.environ.get("FIREBASE_CLIENT_ID"),
        "auth_uri": os.environ.get("FIREBASE_AUTH_URI"),
        "token_uri": os.environ.get("FIREBASE_TOKEN_URI"),
        "auth_provider_x509_cert_url": os.environ.get(
            "FIREBASE_AUTH_PROVIDER_X509_CERT_URL"
        ),
        "client_x509_cert_url": os.environ.get("FIREBASE_CLIENT_X509_CERT_URL"),
    }
)

default_app = initialize_app(cred)


class FirebaseAuthentication(authentication.BaseAuthentication):
    # override authenticate method and write our custom firebase authentication.#

    def authenticate(self, request):
        # Get the authorization Token, It raise exception when no authorization Token is given
        auth_header = request.META.get("HTTP_AUTHORIZATION")
        if not auth_header:
            raise NoAuthToken("No auth token provided")

        # Decoding the Token It rasie exception when decode failed.
        id_token = auth_header.split(" ").pop()
        decoded_token = None
        try:
            decoded_token = auth.verify_id_token(id_token)
        except ValueError:
            raise exceptions.AuthenticationFailed(
                "JWT was found to be invalid, or the App’s project ID cannot "
                "be determined."
            )
        except (
            auth.InvalidIdTokenError,
            auth.ExpiredIdTokenError,
            auth.RevokedIdTokenError,
            auth.CertificateFetchError,
        ) as exc:
            if exc.code == "ID_TOKEN_REVOKED":
                raise exceptions.AuthenticationFailed(
                    "Token revoked, inform the user to reauthenticate or " "signOut()."
                )
            else:
                raise exceptions.AuthenticationFailed("Token is invalid.")

        # Return Nothing
        if not id_token or not decoded_token:
            return None

        # Get the uid of an user
        try:
            uid = decoded_token.get("uid")
            email = decoded_token.get("email")
            name = decoded_token.get("name") or ""
            username = email.split("@").pop(0)
            picture = decoded_token.get("picture")
            now = timezone.now()

        except Exception:
            raise FirebaseError()

        try:
            user = User.objects.get(uid=uid)
        except User.DoesNotExist:
            # if user is not exist, create user
            username_check = User.objects.filter(username=username).exists()
            # 만약 username이 존재한다면, username에 1씩 증가하는 숫자를 붙여준다.
            if username_check:
                num = User.objects.filter(username__startswith=username).count() + 1
                username = f"{username}_{num}"

            user = User.objects.create(
                uid=uid,
                username=username,
                email=email,
                name=name,
                date_joined=now,
                firebase_picture=picture,
            )
            # 가입시 영수증 발행
            PostReceipt.objects.create(user=user)

        user.last_login = now
        user.save()

        # session
        login_time = timezone.datetime.fromtimestamp(
            decoded_token["auth_time"]
        ).astimezone()
        expired_time = timezone.datetime.fromtimestamp(
            decoded_token["exp"]
        ).astimezone()

        user_session, _ = UserSession.objects.get_or_create(
            user=user,
            login_time=login_time,
            defaults={
                "logout_time": None,
                "session_expire_time": expired_time,
                "is_expired": False,
            },
        )

        return (user, None)
