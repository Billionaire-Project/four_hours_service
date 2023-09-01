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
                    "created_at",
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
        "created_at",
        "is_deleted",
    )
    list_display_links = (
        "id",
        "__str__",
    )
    search_fields = [
        "user__username",
    ]
    readonly_fields = (
        "created_at",
        "deleted_at",
    )
