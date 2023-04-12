from rest_framework.serializers import ModelSerializer

from apps.posts.models import post


class PostSerializer(ModelSerializer):
    class Meta:
        model = post.Post
        fields = (
            "id",
            "user",
            "content",
            "created_at",
            "updated_at",
            "is_deleted",
            "deleted_at",
        )
