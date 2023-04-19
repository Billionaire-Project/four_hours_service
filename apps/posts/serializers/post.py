from rest_framework import serializers

from apps.posts.models import Post, PostLike


class PostGetSerializer(serializers.ModelSerializer):
    is_owner = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            "id",
            "user",
            "content",
            "created_at",
            "updated_at",
            "is_owner",
            "is_liked",
        )

    def get_is_owner(self, obj) -> bool:
        return obj.user == self.context.get("request").user

    def get_is_liked(self, obj) -> bool:
        request = self.context.get("request")
        if request.user.is_authenticated:
            return PostLike.objects.filter(
                user=request.user,
                post=obj.id,
            ).exists()
        return False


class PostPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "user",
            "content",
        )
