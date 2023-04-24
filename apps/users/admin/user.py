from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.users.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (
            # admin에서 section을 나눌 수 있음
            "Profile",
            {
                "fields": (
                    # "id", 왜 id가 안나오지?
                    "email",
                    "name",
                    "display_name",
                    "firebase_picture",
                ),
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
                "classes": ("collapse",),
            },
        ),
        (
            "Important dates",
            {
                "fields": (
                    "last_login",
                    "date_joined",
                ),
                "classes": ("collapse",),
            },
        ),
    )
    readonly_fields = (
        "display_name",
        "firebase_picture",
        "last_login",
        "date_joined",
    )
    list_display = (
        "id",
        "email",
        "name",
    )
    list_display_links = (
        "id",
        "email",
    )
