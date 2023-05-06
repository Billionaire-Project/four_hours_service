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
                    "user",
                    "post",
                    "is_postable",
                    "is_readable",
                    "readable_ended_at",
                    "postable_at",
                ),
            },
        ),
    )
    readonly_fields = (
        "user",
        "post",
        "is_postable",
        "is_readable",
        "readable_ended_at",
        "postable_at",
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
