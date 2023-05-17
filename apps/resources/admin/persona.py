from django.contrib import admin

from apps.resources.models import Persona


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    """Persona Admin Definition"""

    fieldsets = (
        (
            "Persona",
            {
                "fields": (
                    "content",
                    "kind",
                    "is_active",
                ),
            },
        ),
    )

    list_display = (
        "id",
        "__str__",
        "kind",
        "is_active",
    )
    list_display_links = (
        "id",
        "__str__",
    )
