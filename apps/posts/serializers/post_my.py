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

    # def to_representation(self, instance):
    #     resp = super().to_representation(instance)
    #     resp["id"] = str(resp["id"])

    #     return resp
