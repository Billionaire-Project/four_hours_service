from rest_framework import serializers

from apps.posts.models import Post


class PostMySerializer(serializers.ModelSerializer):
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            "id",
            "content",
            "created_at",
            "updated_at",
            "is_owner",
        )

    def get_is_owner(self, obj) -> bool:
        return True

    # def to_representation(self, instance):
    #     resp = super().to_representation(instance)
    #     resp["id"] = str(resp["id"])

    #     return resp
