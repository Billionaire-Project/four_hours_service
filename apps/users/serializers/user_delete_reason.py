from rest_framework import serializers

from apps.users.models import UserDeleteReason


class UserDeleteReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDeleteReason
        fields = (
            "id",
            "reason",
        )
