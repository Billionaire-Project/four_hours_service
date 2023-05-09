from rest_framework import serializers

from apps.posts.models import PostObscured


class PostObscuredSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostObscured
        fields = (
            "id",
            "obscured_content",
        )

    # def to_representation(self, instance):
    #     resp = super().to_representation(instance)
    #     resp["id"] = str(resp["id"])

    #     return resp
