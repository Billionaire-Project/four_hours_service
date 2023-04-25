from django.contrib import admin

from apps.posts.models import PostReceipt


@admin.register(PostReceipt)
class PostReceiptAdmin(admin.ModelAdmin):
    """PostReceipt Admin Definition"""

    def has_add_permission(self, request, obj=None):
        return False

    fieldsets = (
        (
            "PostReceipt",
            {
                "fields": (
                    # "id",
                    "post",
                    "user",
                    "is_valid",
                    "shared_post_available_at",
                    "next_post_available_at",
                    "post_delete_stack",
                ),
            },
        ),
    )

    list_display = (
        "id",
        "__str__",
        "post",
        "user",
    )
    list_display_links = (
        "id",
        "__str__",
    )
