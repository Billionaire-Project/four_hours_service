from rest_framework import status
from rest_framework import exceptions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.users.serializers import UserDeleteReasonSerializer


class UserDeleteReason(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_delete_reason = UserDeleteReason.objects.filter(is_public=True)
        serializer = UserDeleteReasonSerializer(user_delete_reason, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
