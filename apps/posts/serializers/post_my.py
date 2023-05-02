from rest_framework import serializers

from apps.posts.models import Post


class PostMySerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "content",
            "created_at",
            "updated_at",
        )
