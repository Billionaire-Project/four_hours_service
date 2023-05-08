from rest_framework import serializers

from apps.posts.models import Post, PostLike, PostReport


class PostGetSerializer(serializers.ModelSerializer):
    is_owner = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    is_reported = serializers.SerializerMethodField()
    # user = serializers.SerializerMethodField() # 나중에 유저 상세정보가 필요하다면 추가하자

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
            "is_reported",
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

    def get_is_reported(self, obj) -> bool:
        request = self.context.get("request")
        if request.user.is_authenticated:
            return PostReport.objects.filter(
                user=request.user,
                post=obj.id,
            ).exists()

    def to_representation(self, instance):
        resp = super().to_representation(instance)
        resp["id"] = str(resp["id"])

        return resp

    # def get_user(self, obj):
    #     return {
    #         "id": obj.user.id,
    #         "name": obj.user.name,
    #         "username": obj.user.username,
    #     }


class PostPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "user",
            "content",
        )
