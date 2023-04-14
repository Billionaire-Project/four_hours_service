from django.contrib import admin

from apps.posts.models import PostDeleteReason


@admin.register(PostDeleteReason)
class PostDeleteReasonAdmin(admin.ModelAdmin):
    """Post Admin Definition"""

    # show all fields in admin
    list_display = (
        "id",
        "__str__",
        "is_public",
    )

    list_display_links = (
        "id",
        "__str__",
    )

    def __str__(self):
        return self.reason
