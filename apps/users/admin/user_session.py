from django.contrib import admin
from apps.users.models import UserSession


@admin.register(UserSession)
class UserSessionAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Profile",
            {
                "fields": (
                    "user",
                    "login_time",
                    "logout_time",
                    "session_expire_time",
                    "is_expired",
                ),
            },
        ),
    )
    readonly_fields = (
        "user",
        "login_time",
        "logout_time",
        "session_expire_time",
        "is_expired",
    )
    list_display = (
        "id",
        "user",
        "login_time",
        "logout_time",
        "session_expire_time",
        "is_expired",
    )
    list_display_links = (
        "id",
        "user",
    )
