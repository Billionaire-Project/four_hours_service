from django.contrib import admin

from apps.resources.models import PostGenerated

from django.contrib.admin import SimpleListFilter


class ActiveFilter(SimpleListFilter):
    title = "is_active"
    parameter_name = "is_active"

    def __init__(self, request, params, model, model_admin):
        # set default value to false
        if "is_active" not in params:
            # params = params.copy()
            # 이렇게 하면 all 필터는 안먹힘
            params["is_active"] = "false"
        super().__init__(request, params, model, model_admin)

    def lookups(self, request, model_admin):
        return (
            ("true", "True"),
            ("false", "False"),
        )

    def queryset(self, request, queryset):
        if self.value() == "true":
            return queryset.filter(is_active=True)
        if self.value() == "false":
            return queryset.filter(is_active=False)


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
        "is_active",
    )
    list_display_links = (
        "id",
        "__str__",
    )
    readonly_fields = (
        "article",
        "persona_preset",
        "persona_situation",
        "topic",
        "time_taken",
        "total_token",
        "is_failed",
    )
    list_filter = [ActiveFilter]
    list_per_page = 10
