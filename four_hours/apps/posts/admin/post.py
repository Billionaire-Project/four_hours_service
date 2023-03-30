from django.contrib import admin

from apps.posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post Admin Definition"""
    # show all fields in admin
    list_display = (
        "__str__",
        "content",
        "user",
    )
