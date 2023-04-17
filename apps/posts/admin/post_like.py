from django.contrib import admin

from apps.posts.models import PostLike


@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
    """PostLike Admin Definition"""

    list_display = (
        "id",
        "user",
        "post",
    )

    list_display_links = (
        "id",
        "user",
        "post",
    )
