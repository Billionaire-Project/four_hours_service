from django.contrib import admin

from apps.resources.models import PersonaCharacteristic


@admin.register(PersonaCharacteristic)
class PersonaCharacteristicAdmin(admin.ModelAdmin):
    """PersonaCharacteristic Admin Definition"""

    fieldsets = (
        (
            "PersonaCharacteristic",
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
