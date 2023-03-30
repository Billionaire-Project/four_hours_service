from rest_framework.serializers import ModelSerializer

from apps.posts.models import post


class PostSerializer(ModelSerializer):
    class Meta:
        model = post
        fields = (
            "title",
        )
