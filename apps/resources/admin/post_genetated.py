from typing import Any
from django.contrib import admin

from apps.resources.models import PostGenerated

from django.contrib.admin import SimpleListFilter


class CheckedFilter(SimpleListFilter):
    title = "is_checked"
    parameter_name = "is_checked"

    def __init__(self, request, params, model, model_admin):
        # set default value to false
        if "is_checked" not in params:
            # params = params.copy()
            # 이렇게 하면 all 필터는 안먹힘
            params["is_checked"] = "false"
        super().__init__(request, params, model, model_admin)

    def lookups(self, request, model_admin):
        return (
            ("true", "True"),
            ("false", "False"),
        )

    def queryset(self, request, queryset):
        if self.value() == "true":
            return queryset.filter(is_checked=True)
        if self.value() == "false":
            return queryset.filter(is_checked=False)


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
                    "is_accepted",
                    "who_checked",
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
        "is_checked",
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
        "who_checked",
    )
    list_filter = [CheckedFilter, "is_accepted"]
    list_per_page = 10

    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        obj.who_checked = request.user
        obj.is_checked = True
        obj.save()
        return super().save_model(request, obj, form, change)
