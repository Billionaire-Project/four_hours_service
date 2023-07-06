from datetime import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework import exceptions
from rest_framework.status import HTTP_200_OK
from firebase_admin import auth


from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from apps.users.models import User, UserDeleteReason
from apps.users.models.user_session import UserSession
from apps.users.serializers.me import MeSerializer


class UserDelete(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="""
        ## 회원탈퇴 시 요청하는 api
        """,
        # manual_parameters=[
        #     openapi.Parameter(
        #         "reason",
        #         openapi.IN_QUERY,
        #         description="삭제 이유의 id",
        #         type=openapi.TYPE_INTEGER,
        #         default=1,
        #     ),
        # ],
    )
    def delete(self, request):
        user = User.objects.get(id=request.user.id)
        uid = user.uid

        try:
            if user.is_deleted:
                raise exceptions.NotFound
            try:
                auth.delete_user(uid)
            except auth.FirebaseError:
                raise exceptions.NotFound

            # 우선 세션 만료
            sessions = UserSession.objects.filter(
                user=request.user, logged_out_at__isnull=True
            )
            session = sessions.last()
            session.logged_out_at = timezone.now()
            session.is_expired = True
            session.save()

            # 서버에서 유저 삭제 처리
            user.is_deleted = True
            user.deleted_at = timezone.now()
            user.save()

        except ValueError:
            raise exceptions.NotFound

        except auth.FirebaseError:
            raise exceptions.NotFound

        return Response(status=HTTP_200_OK)
