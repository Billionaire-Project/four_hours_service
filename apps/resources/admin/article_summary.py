from django.contrib import admin

from apps.resources.models import ArticleSummary


@admin.register(ArticleSummary)
class ArticleSummaryAdmin(admin.ModelAdmin):
    """ArticleSummary Admin Definition"""

    fieldsets = (
        (
            "ArticleSummary",
            {
                "fields": (
                    "article",
                    "summary_content",
                    "is_used",
                )
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
            },
        ),
    )

    list_display = (
        "id",
        "article",
        "is_used",
    )
    list_display_links = (
        "id",
        "article",
        "is_used",
    )
    readonly_fields = (
        "id",
        "article",
        "summary_content",
        "is_used",
        "time_taken",
        "total_token",
        "is_failed",
    )
