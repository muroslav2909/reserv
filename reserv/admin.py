from django.contrib import admin

# Register your models here.
from models import DateChecker
from models import DateCheckerBase


class DateCheckerAdmin(admin.ModelAdmin):
    list_display = ["id", "__unicode__", "url", "nationality", "status", "period"]

   # actions = [start_company, stop_company]
    list_filter = ("nationality", "status")


class DateCheckerBaseAdmin(admin.ModelAdmin):
    list_display = ["id", "company", "text", "free_date", "date", "updated"]

    list_filter = ('company', 'date')

admin.site.register(DateChecker, DateCheckerAdmin)
admin.site.register(DateCheckerBase, DateCheckerBaseAdmin)