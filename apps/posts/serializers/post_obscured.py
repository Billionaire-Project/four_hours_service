from rest_framework import serializers

from apps.posts.models import PostObscured


class PostObscuredSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = PostObscured
        fields = (
            "id",
            "user",
            "content",
            "is_owner",
            "created_at",
            "updated_at",
        )

    def get_is_owner(self, obj) -> bool:
        return obj.user == self.context.get("request").user

    def get_content(self, obj) -> str:
        return obj.obscured_content

    # def to_representation(self, instance):
    #     resp = super().to_representation(instance)
    #     resp["id"] = str(resp["id"])

    #     return resp
