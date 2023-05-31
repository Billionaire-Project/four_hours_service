from django.contrib import admin

from apps.resources.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """Article Admin Definition"""

    fieldsets = (
        (
            "Article",
            {
                "fields": (
                    "kind",
                    "title",
                    "content",
                    "url",
                    "is_summary",
                ),
            },
        ),
    )

    list_display = (
        "id",
        "title",
        "is_summary",
    )
    list_display_links = (
        "id",
        "title",
    )
    readonly_fields = (
        "id",
        "kind",
        "title",
        "content",
        "url",
        "is_summary",
    )
