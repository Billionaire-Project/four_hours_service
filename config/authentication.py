import os

from django.utils import timezone

from apps.users.models.user import User
from firebase_admin import auth
from firebase_admin import credentials
from firebase_admin import initialize_app
from rest_framework.authentication import BaseAuthentication

from .exceptions import FirebaseError
from .exceptions import InvalidAuthToken
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


class FirebaseAuthentication(BaseAuthentication):
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
        except Exception:
            raise InvalidAuthToken("Invalid auth token")

        # Return Nothing
        if not id_token or not decoded_token:
            return None

        # Get the uid of an user
        try:
            uid = decoded_token.get("uid")
            email = decoded_token.get("email")
            name = decoded_token.get("name")
            username = email.split("@").pop(0)
            now = timezone.now()

            print(f"debug: {uid}, {email}, {name}, {username}")

        except Exception:
            raise FirebaseError()

        # 여기서 uid는 firebase에서 받아온 것
        # https://firebase.google.com/docs/auth/admin/verify-id-tokens?hl=ko

        # uid에 대해서 고민 좀 해보자
        user, _ = User.objects.get_or_create(
            uid=uid,
            defaults={
                "username": username,
                "email": email,
                "name": name,
                "date_joined": now,
            },
        )

        user.last_login = now
        user.save()

        return (user, None)
