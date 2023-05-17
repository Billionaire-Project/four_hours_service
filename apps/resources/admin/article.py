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
                ),
            },
        ),
    )

    list_display = (
        "id",
        "title",
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
    )
