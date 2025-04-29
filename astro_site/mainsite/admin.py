from django.contrib import admin

# Import the needed models.
from .models import AstroImage, Request, Comment

# Register your models here.


class RequestAdmin(admin.ModelAdmin):
    """
    Request Admin: Controls how requests appear in the admin section.
    """
    readonly_fields = (
        "first_name",
        "last_name",
        "email",
        "comment",
        "sent_time",
    )


class CommentAdmin(admin.ModelAdmin):
    """
    Comment Admin: Controls how comments appear in the admin section.
    """
    readonly_fields = (
        "image",
        "name",
        "email",
        "content",
        "created_at",
    )

# Register all the models that need to appear in admin.
admin.site.register(AstroImage)
admin.site.register(Request, RequestAdmin)
admin.site.register(Comment, CommentAdmin)
