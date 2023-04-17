from django.contrib import admin

from apps.posts.models import PostReport


@admin.register(PostReport)
class PostReportAdmin(admin.ModelAdmin):
    """PostReport Admin Definition"""

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
