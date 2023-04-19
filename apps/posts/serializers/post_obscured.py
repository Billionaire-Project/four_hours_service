from rest_framework import serializers

from apps.posts.models import PostObscured


class PostObscuredSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostObscured
        fields = (
            "id",
            "user",
            "post",
            "obscured_content",
        )
