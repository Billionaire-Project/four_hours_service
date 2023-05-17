from django.contrib import admin

from apps.resources.models import Topic


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    """Topic Admin Definition"""

    fieldsets = (
        (
            "Topic",
            {
                "fields": (
                    # "id",
                    "topic",
                ),
            },
        ),
        (
            "Topic Option",
            {
                "fields": (
                    "is_used",
                    "topic_used_at",
                    "is_use",
                ),
                "classes": ("collapse",),
            },
        ),
    )

    list_display = (
        "id",
        "__str__",
        "is_used",
        "topic_used_at",
        "is_use",
    )
    list_display_links = (
        "id",
        "__str__",
    )
