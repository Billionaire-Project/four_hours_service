from rest_framework import serializers

from apps.posts.models import PostObscured


# TODO: 앞단과 얘기해서 변경해야 할 부분이 많다!
class PostObscuredSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    is_reported = serializers.SerializerMethodField()

    class Meta:
        model = PostObscured
        fields = (
            "id",
            "user",
            "content",
            "created_at",
            "updated_at",
            "is_owner",
            "is_liked",
            "is_reported",
        )

    def get_content(self, obj) -> str:
        return obj.obscured_content

    def get_is_owner(self, obj) -> bool:
        return False

    def get_is_liked(self, obj) -> bool:
        return False

    def get_is_reported(self, obj) -> bool:
        return False

    # def to_representation(self, instance):
    #     resp = super().to_representation(instance)
    #     resp["id"] = str(resp["id"])

    #     return resp
