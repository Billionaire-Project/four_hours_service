from django.contrib import admin
from django.http.request import HttpRequest

from apps.posts.models import PostObscured


@admin.register(PostObscured)
class PostObscuredAdmin(admin.ModelAdmin):
    """PostObscured Admin Definition"""

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False

    fieldsets = (
        (
            "PostObscured",
            {
                "fields": (
                    "user",
                    "post",
                    "obscured_content",
                ),
            },
        ),
        (
            "GPT Feature",
            {
                "fields": (
                    "time_taken",
                    "total_token",
                    "is_failed",
                ),
                # "classes": ("collapse",),
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
    readonly_fields = (
        "user",
        "post",
        "obscured_content",
        "time_taken",
        "total_token",
        "is_failed",
    )
    list_display = (
        "id",
        "__str__",
        "user",
        "post",
    )
    list_display_links = (
        "id",
        "__str__",
    )
