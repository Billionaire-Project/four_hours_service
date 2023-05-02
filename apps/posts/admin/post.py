from django.contrib import admin

from apps.posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post Admin Definition"""

    fieldsets = (
        (
            "Post",
            {
                "fields": (
                    # "id",
                    "user",
                    "content",
                ),
            },
        ),
        (
            "Delete Option",
            {
                "fields": (
                    "is_deleted",
                    "deleted_at",
                ),
                "classes": ("collapse",),
            },
        ),
    )

    list_display = (
        "id",
        "__str__",
        "user",
        "is_deleted",
    )
    list_display_links = (
        "id",
        "__str__",
    )
