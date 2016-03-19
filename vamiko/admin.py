from django.contrib import admin
from models import VisitorMessage, Subscribe


class VisitorMessageAdmin(admin.ModelAdmin):
    list_display = ["id", "__unicode__", "visitor_name", "message_text", "created", "updated"]
    list_search = ("visitor_email", "visitor_name")

admin.site.register(VisitorMessage, VisitorMessageAdmin)

class SubscribeAdmin(admin.ModelAdmin):
    list_display = ["id", "__unicode__", "created", "updated"]
    list_search = ("visitor_email")

admin.site.register(Subscribe, SubscribeAdmin)
