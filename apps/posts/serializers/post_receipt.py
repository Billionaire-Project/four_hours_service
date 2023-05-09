from rest_framework import serializers

from apps.posts.models import PostReceipt


class PostReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostReceipt
        fields = (
            "id",
            "user",
            "post",
            "is_postable",
            "is_readable",
            "readable_ended_at",
            "postable_at",
        )

    # def to_representation(self, instance):
    #     resp = super().to_representation(instance)
    #     resp["id"] = str(resp["id"])

    #     return resp
