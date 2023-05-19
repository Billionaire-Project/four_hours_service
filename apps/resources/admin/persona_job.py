from django.contrib import admin

from apps.resources.models import PersonaJob


@admin.register(PersonaJob)
class PersonaJobAdmin(admin.ModelAdmin):
    """PersonaJob Admin Definition"""

    fieldsets = (
        (
            "PersonaJob",
            {
                "fields": ("content",),
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
