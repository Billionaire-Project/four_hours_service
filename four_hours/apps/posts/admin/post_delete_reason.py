from django.contrib import admin

from apps.posts.models import PostDeleteReason


@admin.register(PostDeleteReason)
class PostDeleteReasonAdmin(admin.ModelAdmin):
    """Post Admin Definition"""

    # show all fields in admin
    list_display = (
        "__str__",
        "reason",
        "is_public",
    )

    def __str__(self):
        return self.reason
