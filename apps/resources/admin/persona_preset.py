from django.contrib import admin

from apps.resources.models import PersonaPreset


@admin.register(PersonaPreset)
class PersonaPresetAdmin(admin.ModelAdmin):
    """PersonaPreset Admin Definition"""

    fieldsets = (
        (
            "PersonaPreset",
            {
                "fields": (
                    "name",
                    "age",
                    "gender",
                    "job",
                    "tone",
                    "characteristic",
                ),
            },
        ),
    )

    list_display = (
        "id",
        "name",
        "age",
        "gender",
        "job",
    )

    list_display_links = (
        "id",
        "name",
    )
