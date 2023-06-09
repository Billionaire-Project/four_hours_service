from rest_framework import serializers

from apps.posts.models import PostDeleteReason


class PostDeleteReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostDeleteReason
        fields = (
            "id",
            "reason",
        )
