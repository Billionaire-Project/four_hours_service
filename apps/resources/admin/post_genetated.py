from django.contrib import admin

from apps.resources.models import PostGenerated


@admin.register(PostGenerated)
class PostGeneratedAdmin(admin.ModelAdmin):
    """PostGenerated Admin Definition"""

    fieldsets = (
        (
            "PostGenerated",
            {
                "fields": (
                    "content",
                    "article",
                    "persona_preset",
                    "persona_situation",
                    "topic",
                    "is_active",
                ),
            },
        ),
        (
            "Gpt Feature",
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
        "__str__",
        "persona_preset",
    )
    list_display_links = (
        "id",
        "__str__",
        "persona_preset",
    )
    readonly_fields = (
        "content",
        "article",
        "persona_preset",
        "persona_situation",
        "topic",
        "is_active",
    )
