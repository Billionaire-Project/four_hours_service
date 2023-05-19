from django.contrib import admin

from apps.resources.models import PersonaSituation


@admin.register(PersonaSituation)
class PersonaSituationAdmin(admin.ModelAdmin):
    """PersonaSituation Admin Definition"""

    fieldsets = (
        (
            "PersonaSituation",
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
