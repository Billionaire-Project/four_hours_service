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
                    "persona_job",
                    "persona_gender",
                    "persona_age",
                    "persona_tone",
                    "persona_situation",
                    "persona_characteristic",
                    "persona_topic",
                    "topic",
                    "article",
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
                # "classes": ("collapse",),
            },
        ),
    )

    list_display = (
        "id",
        "__str__",
    )
    list_display_links = (
        "id",
        "__str__",
    )
    readonly_fields = (
        "content",
        "persona_job",
        "persona_gender",
        "persona_age",
        "persona_tone",
        "persona_situation",
        "persona_characteristic",
        "persona_topic",
        "topic",
        "is_active",
        "article",
        "time_taken",
        "total_token",
        "is_failed",
    )
