from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.users.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    form = UserAdmin.form
    fieldsets = (
        (
            # admin에서 section을 나눌 수 있음
            "Profile",
            {
                "fields": (
                    # "id",
                    "name",
                    "username",
                    "email",
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
        "username",
        "firebase_picture",
        "last_login",
        "date_joined",
    )
    list_display = (
        "id",
        "username",
        "email",
    )
    list_display_links = (
        "id",
        "username",
        "email",
    )
    search_fields = (
        "username",
        "name",
    )
