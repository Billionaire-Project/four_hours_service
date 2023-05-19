from django.contrib import admin

from apps.resources.models import PersonaTone


@admin.register(PersonaTone)
class PersonaToneAdmin(admin.ModelAdmin):
    """PersonaTone Admin Definition"""

    fieldsets = (
        (
            "PersonaTone",
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
